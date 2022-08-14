# coding=utf-8
from loguru import logger
import json
import asyncio
import aioredis
from oceanwebsocket.websocketconfig import *
from message.message_push_client import *
from loguru import logger
from message.template.message_obsever import *


class MessagePullRedis(object):
    async def read_message_from_redis(self):
      logger.debug(f"read_message_from_redis_start")

      redis = aioredis.from_url(websocketconfig_instance.get_auth_token())
      while True:
        result = await redis.xreadgroup(
          groupname="consumer_group_1", 
          consumername="client_1", 
          streams={"oceanmonitor_stream":">"}, 
          count=1, 
          block=0)
        logger.debug(f"read_message_from_redis={result}")
