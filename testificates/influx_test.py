import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import constants as const
import psutil as pc

write_client = influxdb_client.InfluxDBClient(url = const.URL, token = const.TOKEN, org = const.ORG)

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(100):
  point = (
    Point("cpu_load")
    .tag("comp", "local")
    .field("cpu_load_percent", pc.cpu_percent())
  )
  write_api.write(bucket = const.BUCKET, org = const.ORG, record = point)
  time.sleep(0.5)

read_api = write_client.query_api()

query = '''from(bucket: "main")
  |> range(start: -45m)
  |> filter(fn: (r) => r["_measurement"] == "cpu_load")'''
print(read_api.query(org = const.ORG, query = query).to_json())
