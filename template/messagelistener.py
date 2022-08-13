# coding=utf-8
from loguru import logger


class MessageListener:
    def __init__(self):
      self.obsever_list = {}

    def add_observer(self, unique_key -> str, msg_observer -> object):
      self.obsever_list.update({unique_key,  msg_observer})

    def get_message_instance(self, msg_source -> dict):
      if msg_source.get('channel_id') == None:
        logger.error(f"dict get channel_id error {msg_source}")
        return None
      if msg_source.get('web_site_name') == None:
        logger.error(f"dict get web_site_name error {msg_source}")
        return None

      unique_key = msg_source.get('channel_id') + msg_source.get('web_site_name')
      return self.obsever_list.get(unique_key)
