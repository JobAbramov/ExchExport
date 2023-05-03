import datetime as dt
from binance.client import Client
from binance.enums import KLINE_INTERVAL_1MINUTE, HistoricalKlinesType
import sys
from dotenv import get_key

API_KEY = get_key('.env', 'API_KEY')
API_SECRET = get_key('.env', 'API_SECRET')

client = Client(api_key = API_KEY,api_secret = API_SECRET)

try:
    result = client.get_historical_klines('BTCUSDT', KLINE_INTERVAL_1MINUTE, '2023-04-01', '2023-04-02', klines_type = HistoricalKlinesType.SPOT)
except Exception as e:
    print('Exception occured! ', e)
    sys.exit()

for item in result:
    print('Open time: {}, Open price: {}, High price: {}, Low price: {}, Close price: {}, Volume: {}'.format(dt.datetime.fromtimestamp(item[0] / 1e3), item[1], item[2], item[3], item[4], item[5]))

print('# data entries fetched:' , len(result))

