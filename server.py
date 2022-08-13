# coding=utf-8
from oceanwebsocket.oceanwebsocket import OceanWebSocketServer
from utils.oceanlogger import OceanLogger


class Server:
    def __init__(self):
      # 初始化logger 配置
      OceanLogger()

    def start(self):
      OceanWebSocketServer().start()

if __name__ == "__main__":
    server = Server()
    server.start()
