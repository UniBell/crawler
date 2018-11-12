import asyncio
import websockets
import json
from crawler.manager import db
from crawler.manager.model import OrderBook

async def bitmex():
    async with websockets.connect(
        'wss://www.bitmex.com/realtime') as websocket:
        param = {"op": "subscribe", "args": ["orderBook10:XBTUSD"]}
        await websocket.send(json.dumps(param))
        
        while True:
            resp = await websocket.recv()
            result = json.loads(str(resp))
            if 'data' in result.keys():
                data = result['data'][0]
                print(data)
                dict = {
                    'symbol': data['symbol'],
                    'timestamp': data['timestamp'],
                    'bids': json.dumps(data['bids']),
                    'asks': json.dumps(data['asks'])
                }
                order = OrderBook(**dict)
                print(order)
                db.session.add(order)
                db.session.commit()
                break        

asyncio.get_event_loop().run_until_complete(bitmex())

if __name__ == '__main__':
    bitmex()

#旧写法
# from ws4py.client.threadedclient import WebSocketClient
# import json

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