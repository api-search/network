---
aid: new-relic:new-relic-sendmetrics
name: New Relic Send metric data
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Sends an array of metric data points to the New Relic Metric API. The request body must be a JSON array of metric data objects, each containing a metrics array and optional common attributes. Payloads should be gzip-compressed for best performance. The API supports count, gauge, and summary metric types.

---
