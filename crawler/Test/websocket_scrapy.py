# from ws4py.client.threadedclient import WebSocketClient
import asyncio
import websockets
import json

# {'table': 'orderBookL2', 'action': 'update', 'data': [{'symbol': 'XBTUSD', 'id': 8799997000, 'side': 'Buy', 'size': 35}]}

async def bitmex():
    async with websockets.connect(
        'wss://www.bitmex.com/realtime') as websocket:
        param = {"op": "subscribe", "args": ["orderBookL2:XBTUSD"]}
        await websocket.send(json.dumps(param))
        
        while True:
            resp = await websocket.recv()
            data = json.loads(str(resp))
            # print(data)            

asyncio.get_event_loop().run_until_complete(bitmex())

#旧写法
# class BT_Client(WebSocketClient):
   
#    def opened(self):
#        req = '{"op":"subscribe", "args": ["orderBookL2:XBTUSD"]}'
#        self.send(req)
   
#    def closed(self, code, reason=None):
#        print("Closed down:", code, reason)
   
#    def received_message(self, resp):
#        resp = json.loads(str(resp))
#        # data = resp['data']
#        print(resp)


# if __name__ == '__main__':
#    ws = None
#    try:
#        ws = BT_Client('wss://www.bitmex.com/realtime')
#        ws.connect()
#        ws.run_forever()
#    except KeyboardInterrupt:
#        ws.close()