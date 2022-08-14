# coding=utf-8
from loguru import logger
from utils.singleton import *
from utils.oceanlogger import *
from message.template.message_obsever import *
from message.template.ominous863023145463578644 import *
from message.template.prism863023145463578644 import *


@singleton
class MessageFactory(object):
    def __init__(self):
      self.obsever_list = {}

    @logger.catch
    def get_message_instance(self, msg_source: dict) -> MessageObsever:
      if msg_source.get('channel_id') == None:
        logger.error(f"dict get channel_id error {msg_source}")
        return None
      if msg_source.get('web_site_name') == None:
        logger.error(f"dict get web_site_name error {msg_source}")
        return None

      unique_key = msg_source.get('web_site_name') + msg_source.get('channel_id')
      if unique_key == 'Ominous863023145463578644':
        message_obsever = Ominous863023145463578644()
      elif unique_key == 'Prism863023145463578644':
        message_obsever = Prism863023145463578644()
      else:
        logger.error(f"unique_key={unique_key} | msg_source={msg_source}")
        return None

      message_obsever.init(msg_source)
      logger.info(f"message_obsever={message_obsever}")
      return message_obsever


messagefactory_instance = MessageFactory()
