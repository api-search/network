---
description: A single metric series containing data points and associated metadata
layout: schema
name: MetricSeries
properties_list:
- description: The name of the metric to submit. Must not exceed 200 characters. Only ASCII alphanumerics, underscores, and periods are allowed.
  name: metric
  type: string
- description: The type of the metric (0=unspecified, 1=count, 2=rate, 3=gauge)
  name: type
  type: integer
- description: List of data points, each containing a timestamp (Unix epoch in seconds) and a value
  name: points
  type: array
- description: List of tags associated with the metric in key:value format (e.g., env:prod)
  name: tags
  type: array
- description: The name of the host that produced the metric data
  name: host
  type: string
- description: A list of resources associated with the metric, such as hosts or services
  name: resources
  type: array
- description: If the type is rate or count, defines the corresponding interval in seconds
  name: interval
  type: integer
- description: The unit of the metric value (e.g., byte, second, request)
  name: unit
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-metrics-metric-series-schema.json
slug: datadog-metrics-metric-series
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MetricSeries
---
