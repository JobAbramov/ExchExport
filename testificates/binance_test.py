from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime as dt
from binance.client import Client
import sys

client = Client("","")

try:
    result = client.get_historical_klines('BTCUSDT', '1h', '2023-04-01', '2023-04-02')
except Exception as e:
    print('Exception occured! ', e)
    sys.exit()

print('# data enties fetched:' , len(result))

for item in result:
    print('Close price: {}, Volume: {}, Close time: {}'.format(item[4], item[5], dt.datetime.fromtimestamp(item[6] / 1e3)))



