# coding=utf-8
from loguru import logger
import json
import asyncio
import aioredis
from oceanwebsocket.websocketconfig import *
from loguru import logger
from message.template.message_obsever import *


class MessagePullRedis(object):
    def start(self):
      asyncio.gather(self.read_message_from_redis())

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

        logger.debug(f"read_message_from_redis={result}")
