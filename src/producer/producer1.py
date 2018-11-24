import time

from datetime import datetime
from dateutil import parser

import influxdb

from binance.client import Client


api_key = 'R8IDlMMU1fuIwrEA3uIUldlMUJDfCir30cNnKdcnKBwih0Qajk8abp4eHSYCGiKg'
api_secret = 'ElGk1n5Ce4h96d0pO78bAGSt31zo5hky3jLa82CTx5Oi4LUdJhB1YJ7rdPyHnVDo'

client = Client(api_key, api_secret)
symbols = {
    s['symbol']: {'baseAsset': s['baseAsset'], 'quoteAsset': s['quoteAsset']}
    for s in client.get_exchange_info()['symbols']
}

DATA = []
TIME = time.time()
influx_client = influxdb.InfluxDBClient(host='influxdb', database='raw_trade_data')


def process_message(msg):
    global DATA, TIME
    to_float = (
        lambda obj, key:
        float(obj[key])
        if obj.get(key) else float(0)
    )
    to_time = (
        lambda t:
        parser.parse(t)
        if type(t) == str else datetime.utcfromtimestamp(t / 1000)
    )
    DATA.append({
        'measurement': 'trades',
        'time': to_time(msg['T']),
        'tags': {
            'symbol': msg['s'],
            'exchange': 'BINANCE',
            'provider': 'BINANCE_SOCKET'
        },
        'fields': {
            'price': to_float(msg, 'p'),
            'volume': to_float(msg, 'q')
        }
    })
    if (time.time() - TIME) > 3:
        influx_client.write_points(DATA)
        DATA = []
        TIME = time.time()


from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
for symbol in symbols:
    bm.start_aggtrade_socket(symbol, process_message)
bm.start()

#'https://hooks.slack.com/services/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'