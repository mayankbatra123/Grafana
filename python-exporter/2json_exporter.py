from prometheus_client import start_http_server, Metric, REGISTRY
import json
import requests
import sys
import time

class JsonCollector(object):
  def __init__(self, endpoint):
    self._endpoint = endpoint
  def collect(self):
    # Fetch the JSON
    response = json.loads(requests.get(self._endpoint).content.decode('UTF-8'))

    # Convert requests and duration to a summary in seconds
    metric = Metric('Active_Cases_time',
        'Active cases in time series', 'summary')
    for i in response['cases_time_series']:
        dte=i['date']
        metric.add_sample('total_confirmed_cases',
            value=i['totalconfirmed'], labels={'date':dte})
        metric.add_sample('total_recovered_cases',
            value=i['totalrecovered'], labels={'date':dte})
    yield metric


if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int(sys.argv[1]))
  REGISTRY.register(JsonCollector(sys.argv[2]))

  while True: time.sleep(1)
