---
description: The result of a metric query, containing time-series data for each requested metric and dimension combination.
layout: schema
name: MetricData
properties_list:
- description: The resolution of the data points in the response. For example, 1h means each data point represents one hour of data.
  name: resolution
  type: string
- description: The cursor for the next page of results if the response is paginated. Null if all results are returned.
  name: nextPageKey
  type: string
- description: The total number of data series in the result.
  name: totalCount
  type: integer
- description: The list of metric series collections, one per metric key matched by the selector.
  name: result
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-metrics-v2-metric-data-schema.json
slug: dynatrace-metrics-v2-metric-data
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
title: MetricData
---
