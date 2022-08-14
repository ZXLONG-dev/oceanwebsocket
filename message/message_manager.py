# coding=utf-8
from re import I
from loguru import logger
import json
import asyncio
import aioredis
from ..oceanwebsocket.userclient import UserClient
from oceanwebsocket.websocketconfig import *
from loguru import logger
from message.template.message_obsever import *
from utils.singleton import *


@singleton
class MessageManager(object):
    def __init__(self):
        self.connect_client_list = []

    def listen(self):
      asyncio.gather(self.read_message_from_redis())

    def processing(self, client_ws, message: dict):
      pass

    def add_user_client(self, connect_client: UserClient):
      self.connect_client_list.append(connect_client)

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

        for user_client in self.connect_client_list:
          await user_client.send_content(result)


message_manager = MessageManager()
