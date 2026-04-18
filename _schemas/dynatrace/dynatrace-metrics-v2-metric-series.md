---
description: A single time series representing metric values for a specific combination of dimension values over a time range.
layout: schema
name: MetricSeries
properties_list:
- description: 'A map of dimension names to their values for this specific series. For example, {"host": "web-01", "environment": "production"}.'
  name: dimensionMap
  type: object
- description: An ordered list of dimension values corresponding to the metric's dimension definitions.
  name: dimensions
  type: array
- description: Unix timestamps in milliseconds for each data point in the series. Aligns one-to-one with the values array.
  name: timestamps
  type: array
- description: Metric values corresponding to each timestamp. A null value indicates no data was recorded for that time slot (gap in the data).
  name: values
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-metrics-v2-metric-series-schema.json
slug: dynatrace-metrics-v2-metric-series
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: MetricSeries
---
