---
description: A single metric data point
layout: schema
name: MetricDataPoint
properties_list:
- description: The metric name (e.g., cpu.usage.percent)
  name: name
  type: string
- description: The metric type
  name: type
  type: string
- description: The metric value. For gauge and count, a number. For summary, an object with count, sum, min, and max fields.
  name: value
  type: object
- description: Unix timestamp in milliseconds. Overrides the common timestamp for this metric.
  name: timestamp
  type: integer
- description: Measurement interval in milliseconds. Required for count and summary types.
  name: interval.ms
  type: integer
- description: Additional key-value attributes for this metric point
  name: attributes
  type: object
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/metric-api-metric-data-point-schema.json
slug: metric-api-metric-data-point
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
title: MetricDataPoint
---
