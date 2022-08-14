# coding=utf-8
from loguru import logger
import json
from utils.oceanlogger import *
from message.template.message_obsever import *


class Prism863023145463578644(MessageObsever):
    def __str__(self):
      class_str_desc = f"message_id={self.message_id}|source_datea={self.source_data}"
      return class_str_desc

    def init(self, source_data: dict):
      self.source_data = source_data
      self.message_id = self.source_data.get("id")
      self.webhook_id = "863023145463578644"
      self.web_site = "prism"

    def get_serialize_data(self) -> str:
      return json.dumps(self.source_data)
