import aiohttp
import asyncio
import json


async def keep_connect(ws):
    keep_times = 1
    while True:
        content = {}
        content["opt"] = "keep_connect"
        content["value"] = keep_times

        await ws.send_str(json.dumps(content))
        keep_times += 1
        await asyncio.sleep(1)


async def connect(ws):
    content = {}
    content["opt"] = "connect"
    content["auth"] = ""
    await ws.send_str(json.dumps(content))


async def main():
    async with aiohttp.ClientSession() as session:
       async with session.ws_connect('ws://127.0.0.1:8080') as ws:
           await connect(ws)
           asyncio.create_task(keep_connect(ws))
           async for msg in ws:
               print(f'{msg}')
               if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == 'close cmd':
                        await ws.close()
                        break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
