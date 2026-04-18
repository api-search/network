---
description: A collection of time-series data for a single metric key, containing one series per unique dimension combination.
layout: schema
name: MetricSeriesCollection
properties_list:
- description: The metric key for this collection, including any applied transformations.
  name: metricId
  type: string
- description: The list of individual time series, one per unique combination of dimension values.
  name: data
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/metrics-api-v2-metric-series-collection-schema.json
slug: metrics-api-v2-metric-series-collection
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
title: MetricSeriesCollection
---
