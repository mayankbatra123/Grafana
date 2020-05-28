# Grafana
Dashboard with Prometheus and Grafana - Sample with Covid19 API data

API used
- https://api.covid19india.org/state_district_wise.json
- https://api.covid19india.org/data.json

Python Script :
- To convert API data to Time Series Data for Prometheus to Consume
- Server Data on 31001 and 31000 port.

Prometheus:
- Pull prometheus docker images and run with port mapping.
- Make sure to have prometheus.yaml file in $PWD/config directory.

Grafana:
- Launch Grafana instance on kubernetes using persistance volume.



