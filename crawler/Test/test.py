import json
from crawler.manager import db
from crawler.manager.model import OrderBook

def test():
    dict = {
        'symbol': 'XBTUSD',
        'timestamp': '2018-11-08T10:23:49.320Z',
        'bids': json.dumps([[6458, 1988549], [6457.5, 446935], [6457, 115116], [6456.5, 33282], [6456, 147829], [6455.5, 60852], [6455, 982807], [6454.5, 171761], [6454, 291050], [6453.5, 364603]]),
        'asks': json.dumps([[6458.5, 4412249], [6459, 312611], [6459.5, 77186], [6460, 277318], [6460.5, 218971], [6461, 343609], [6461.5, 124422], [6462, 189722], [6462.5, 477059], [6463, 818641]])
    }
    order = OrderBook(**dict)
    db.session.add(order)
    db.session.commit()