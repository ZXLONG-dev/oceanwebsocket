# coding=utf-8
from utils.oceanlogger import *
from abc import ABCMeta, abstractclassmethod


class MessageObsever(metaclass=ABCMeta):
    @abstractclassmethod
    def init(self, source_data: dict):
        pass

    @abstractclassmethod
    def get_serialize_data(self) -> str:
        pass
