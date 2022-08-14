import json
from loguru import logger


class UserClient:
    def __init__(self, client_ws, ip, version):
        self.client_ws = client_ws
        self.version = version
        self.ip = ip

    @logger.catch
    async def send_content(self, content):
        await self.client_ws.send_str(content)

    @logger.catch
    async def disconnect(self):
        content = {}
        content["opt"] = "keep_connect_close"
        await self.send_content(json.dumps(content))
        await self.client_ws.close()
