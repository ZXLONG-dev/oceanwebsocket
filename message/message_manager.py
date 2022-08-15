# coding=utf-8
from concurrent.futures.process import _chain_from_iterable_of_lists
from loguru import logger
import json
import asyncio
import aioredis
from oceanwebsocket.userclient import UserClient
from oceanwebsocket.websocketconfig import *
from loguru import logger
from message.template.message_obsever import *
from utils.singleton import *


@singleton
class MessageManager(object):
    def __init__(self):
        self.connect_client_list = {}


    @logger.catch
    async def client_connect(self, client_ws, message) -> bool:
      user_key = message.get("auth")
      if user_key == None:
        error_msg = {"error_code": "NOAUTH", "error_msg": "connect server not auth"}
        logger.error(f"{error_msg}")
        await client_ws.send_json(error_msg)
        return False

      user_client = UserClient(client_ws, user_key)
      if not user_client.check_vaild():
        error_msg = {"error_code": "NOAUTH", "error_msg": "connect server not auth"}
        logger.error(f"{error_msg}")
        await client_ws.send_json(error_msg)
        return False

      self.connect_client_list[user_key] = user_client
      return True

    @logger.catch
    async def processing(self, client_ws, message: dict):
      logger.debug(f"{message}")

      if message.get('opt') == "connect":
        connected = await self.client_connect(client_ws, message)
        if not connected:
          return

      user_key = message.get("auth")
      if not user_key:
        await client_ws.send_json({"error_code": "BADREQUEST", "error_msg": "request body error"})
        return

      user_client = self.connect_client_list.get(user_key)
      if not user_client:
        await client_ws.send_json({"error_code": "NOAUTH", "error_msg": "connect server not auth"})
        return

      if message.get('opt') == "keep_connect":
        await user_client.keep_connect()

    def listen(self):
      asyncio.gather(self.read_message_from_redis())

    @logger.catch
    async def read_message_from_redis(self):
      while True:
        redis = aioredis.from_url(websocketconfig_instance.get_auth_token())
        result = await redis.xreadgroup(
            groupname="consumer_group_1",
            consumername="client_1",
            streams={"oceanmonitor_stream": ">"},
            count=1,
            block=0,
            noack=True)

        # result [[b'oceanmonitor_stream', [(b'1660573563768-0', {b'test2': b'mnm'})]]]
        # dict byte to dict str
        result = {key.decode(): val.decode() for key, val in result[0][1][0][1].items()}
        logger.debug(f"{json.dumps(result)}")

        for key, user_client in self.connect_client_list.items():
          await user_client.send_content_json(result)


message_manager = MessageManager()
