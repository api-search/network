---
aid: datadog:datadog-submitmetrics
name: Submit metrics
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Submits metrics data points to the Datadog platform. The body should contain a series of metric submissions, each with a metric name, type, data points (timestamp and value pairs), tags, and optional host and resource information. Supports count, rate, gauge, and distribution metric types. The maximum payload size is 512 KB (uncompressed). Each metric series can contain up to 100 data points.

---
