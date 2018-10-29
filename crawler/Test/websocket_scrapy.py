# from ws4py.client.threadedclient import WebSocketClient
import asyncio
import websockets
import json

async def bitmex():
    async with websockets.connect(
        'wss://www.bitmex.com/realtime') as websocket:
        param = {"op": "subscribe", "args": ["orderBookL2:XBTUSD"]}
        await websocket.send(json.dumps(param))
        resp = await websocket.recv()
        print(resp)

asyncio.get_event_loop().run_until_complete(bitmex())
asyncio.get_event_loop().run_forever()