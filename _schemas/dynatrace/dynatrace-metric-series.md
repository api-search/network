---
description: A time-series data series returned by the Dynatrace Metrics API v2 query endpoint, representing metric values for a specific set of dimensions over a time range.
layout: schema
name: Dynatrace Metric Series
properties_list:
- description: The metric key with applied transformations, e.g. builtin:host.cpu.usage:avg. This key identifies the metric and any selector transformations that were applied during the query.
  name: metricId
  type: string
- description: Array of time series, one per unique dimension combination. Each item represents a distinct set of dimension values (e.g., a specific host or service) with its corresponding timestamps and metric valu
  name: data
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-metric-series-schema.json
slug: dynatrace-metric-series
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
title: Dynatrace Metric Series
---
