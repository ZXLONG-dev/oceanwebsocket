# coding=utf-8
from aiohttp import web
from loguru import logger
import aiohttp
import asyncio


class OceanWebSocketServer():
    def start(self):
      WS_HOST = "0.0.0.0"
      PORT = 8080
      app = web.Application()
      app.router.add_get('/', lambda req: self.websocket_handler(req))
      web.run_app(app, host=WS_HOST, port=PORT)

    async def websocket_handler(self, request):
      ws = web.WebSocketResponse()
      await ws.prepare(request)

      async for msg in ws:
          if msg.type == aiohttp.WSMsgType.TEXT:
              if msg.data == 'close':
                  await ws.close()
              else:
                  await ws.send_str(msg.data + '/answer')
          elif msg.type == aiohttp.WSMsgType.ERROR:
              print('ws connection closed with exception %s' %
                    ws.exception())

      print('websocket connection closed')

      return ws
