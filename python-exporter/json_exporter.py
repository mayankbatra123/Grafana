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
    metric = Metric('Active_Cases',
        'Active cases', 'summary')
    for i in response['Haryana']['districtData']:
        metric.add_sample('active_cases',
            value=response['Haryana']['districtData'][i]['active'], labels={'city':i})
    yield metric
    metric = Metric('Recovered_Cases',
        'Recovered cases', 'summary')
    for i in response['Haryana']['districtData']:
        metric.add_sample('recovery_cases',
            value=response['Haryana']['districtData'][i]['recovered'], labels={'city':i})
    yield metric
    metric = Metric('Confirmed_Cases',
        'Confirmed cases', 'summary')
    for i in response['Haryana']['districtData']:
        metric.add_sample('confirmed_cases',
            value=response['Haryana']['districtData'][i]['confirmed'], labels={'city':i})
    yield metric
    metric = Metric('Delhi_Cases',
        'Delhi cases', 'summary')
    for i in response['Delhi']['districtData']:
        for j in ['active','confirmed','recovered']:
            metric.add_sample(j+'_delhi_cases',
                value=response['Delhi']['districtData'][i][j], labels={'city':i})
   # metric.add_sample('ggn_recovered_cases',
   #     value=response['Haryana']['districtData']['Gurugram']['recovered'] , labels={})
   # metric.add_sample('ggn_confirmed_cases',
   #     value=response['Haryana']['districtData']['Gurugram']['confirmed'] , labels={})
   # metric.add_sample('hisar_active_cases',
   #     value=response['Haryana']['districtData']['Hisar']['active'] , labels={})
   # metric.add_sample('hisar_recovered_cases',
   #     value=response['Haryana']['districtData']['Hisar']['recovered'] , labels={})
   # metric.add_sample('hisar_confirmed_cases',
   #     value=response['Haryana']['districtData']['Hisar']['confirmed'] , labels={})
    yield metric


if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int(sys.argv[1]))
  REGISTRY.register(JsonCollector(sys.argv[2]))

  while True: time.sleep(1)
