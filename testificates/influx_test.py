import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import psutil as pc
import dotenv as dnv

URL = dnv.get_key('.env', 'URL')
TOKEN = dnv.get_key('.env', 'TOKEN')
ORG = dnv.get_key('.env', 'ORG')
BUCKET = dnv.get_key('.env', 'BUCKET')

write_client = influxdb_client.InfluxDBClient(url = URL, token = TOKEN, org = ORG)

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(100):
  point = (
    Point("cpu_load")
    .tag("comp", "local")
    .field("cpu_load_percent", pc.cpu_percent())
  )
  write_api.write(bucket = BUCKET, org = ORG, record = point)
  time.sleep(0.5)

read_api = write_client.query_api()

query = '''from(bucket: "main")
  |> range(start: -1d)
  |> filter(fn: (r) => r["_measurement"] == "cpu_load")'''
  
print(read_api.query(org = ORG, query = query).to_json())
