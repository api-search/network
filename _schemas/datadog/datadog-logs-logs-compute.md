---
description: A computation to perform over the filtered log set
layout: schema
name: LogsCompute
properties_list:
- description: The type of aggregation to compute over log events
  name: aggregation
  type: string
- description: The log attribute to aggregate (required for all aggregations except count)
  name: metric
  type: string
- description: Whether this is a total aggregation or a timeseries
  name: type
  type: string
- description: The time interval for timeseries computations (e.g., 1m, 1h, 1d)
  name: interval
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-logs-compute-schema.json
slug: datadog-logs-logs-compute
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: LogsCompute
---
