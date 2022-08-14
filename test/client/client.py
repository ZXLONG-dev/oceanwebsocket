import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
       async with session.ws_connect('ws://127.0.0.1:8000') as ws:
          async for msg in ws:
              print(f'{msg}')

              if msg.type == aiohttp.WSMsgType.TEXT:
                  if msg.data == 'close cmd':
                      await ws.close()
                      break
                  else:
                      await ws.send_str(msg.data + '/answer')
              elif msg.type == aiohttp.WSMsgType.ERROR:
                  break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
