# from ws4py.client.threadedclient import WebSocketClient
import asyncio
import websockets
import json

@asyncio.coroutine
def bitmex():
    websocket = yield from websockets.connect(
        'wss://www.bitmex.com/realtime')
    try:
        param = {"op": "subscribe", "args": ["orderBookL2:XBTUSD"]}
        yield from websocket.send(json.dumps(param))
        resp = yield from websocket.recv()
        print(resp)    
    finally:
        yield from websocket.close()        

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