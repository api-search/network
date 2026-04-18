---
description: A single data point consisting of a Unix timestamp and a numeric value
layout: schema
name: MetricPoint
properties_list:
- description: The Unix timestamp in seconds when this data point was recorded
  name: timestamp
  type: integer
- description: The numeric value of the metric at the given timestamp
  name: value
  type: number
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-metrics-metric-point-schema.json
slug: datadog-metrics-metric-point
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MetricPoint
---
