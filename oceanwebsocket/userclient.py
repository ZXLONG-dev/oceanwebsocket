import json
from loguru import logger


class UserClient:
    def __init__(self, client_ws, user_key):
        self.client_ws = client_ws
        self.user_key = user_key

    def check_vaild(self) -> bool:
        return True

    @logger.catch
    async def keep_connect(self):
        await self.client_ws.send_json({"opt": "connect_return"})

    @logger.catch
    async def send_content(self, content: str):
        await self.client_ws.send_str(content)

    @logger.catch
    async def send_content_json(self, content: dict):
        await self.client_ws.send_json(content)

    @logger.catch
    async def disconnect(self):
        content = {}
        content["opt"] = "keep_connect_close"
        await self.send_content(json.dumps(content))
        await self.client_ws.close()
