import requests
import json

# message_id = '1003891040794718309' # Ominous-863023145463578644
message_id = '1005389494008160308'  # Prism-863023145463578644

target_channel = '863023145463578644'
token = "ODI1OTA5NDE3ODEwOTg0OTgw.GN8HcB.kM3K6jfEH4SsdaCyB4daiCP-2li5QWDt1uaDGI"
target_channel_webhook = "https://discord.com/api/webhooks/863024970543530014/qgQ3rzuiFtGovmfLVNqmNH969Jf12sqsu6XRg9gh1uPnp4tcwuJb1LN8ZzJEh5Hl9Hlb"

getHeader = {
    'accept': '*/*',
    'accept-language': 'zh-CN',
    'authorization': token,
    'cookie': '_ga=GA1.2.245652089.1597657431; __cfduid=dd728c6294f8b4064afb6e0a856c18c281600258495; locale=zh-CN; _gid=GA1.2.1129671544.1601149594',
    'dnt': '1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

pushHeader = {"Content-Type": "application/json"}


def sendMessageViaId():
    sendmsg_url = f'https://discord.com/api/v8/channels/{target_channel}/messages?before={message_id}&limit=1'
    res = requests.get(sendmsg_url, headers=getHeader)
    message = json.loads(res.content.decode('utf8'))[0]
    message["username"] = message["author"]["username"]

    print(message)
    push = requests.post(target_channel_webhook, headers=pushHeader, data=json.dumps(message))
    print(push.text)


if __name__ == "__main__":
    sendMessageViaId()
