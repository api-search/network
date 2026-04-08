---
aid: prometheus:prometheus-deleteseries
name: Prometheus Delete series
tags:
- TSDB
humanURL: 
properties: []
description: >-
  Deletes data for a selection of series in a time range. This only creates tombstones in the TSDB; actual deletion happens on the next compaction. Requires --web.enable-admin-api flag.

---
