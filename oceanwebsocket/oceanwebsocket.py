# coding=utf-8
from aiohttp import web
from loguru import logger
import aiohttp
from message.message_manager import *
import asyncio
from utils.singleton import *


@singleton
class OceanWebSocketServer():
    def start(self):
      WS_HOST = "0.0.0.0"
      PORT = 8080
      app = web.Application()
      app.router.add_get('/', lambda req: self.websocket_handler(req))
      web.run_app(app, host=WS_HOST, port=PORT, loop=asyncio.get_event_loop())

    @logger.catch
    async def websocket_handler(self, request):
      ws = web.WebSocketResponse(autoclose=False)
      await ws.prepare(request)
      await ws.send_str("hello world\n")

      async for msg in ws:
          if msg.type == aiohttp.WSMsgType.TEXT:
            message = json.loads(msg.data)
            await message_manager.processing(ws, message)
          elif msg.type == aiohttp.WSMsgType.ERROR:
              await ws.close()
              logger.error(f"ws connection exception {ws.exception()}")


oceanwebsocketserver = OceanWebSocketServer()
