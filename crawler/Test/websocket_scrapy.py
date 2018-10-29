from ws4py.client.threadedclient import WebSocketClient
import json

class BT_Client(WebSocketClient):
    
    def opened(self):
        req = '{"op":"subscribe", "args": ["orderBookL2:XBTUSD"]}'
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        # data = resp['data']
        print(resp)


if __name__ == '__main__':
    ws = None
    try:
        ws = BT_Client('wss://www.bitmex.com/realtime')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()