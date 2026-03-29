---
aid: cloudwatch:cloudwatch-putmetricdata
name: Publish metric data points to CloudWatch
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to ListMetrics. Each PutMetricData request is limited to 1 MB in size for HTTP POST requests and is limited to 40 KB for HTTP GET requests. The maximum number of metric datum items per PutMetricData request i...

---
