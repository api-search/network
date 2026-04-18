---
description: A single timeseries result for a query formula
layout: schema
name: TimeseriesResult
properties_list:
- description: Index of the query or formula that produced this result
  name: query_index
  type: integer
- description: Unit information for the metric values in this series
  name: unit
  type: array
- description: The tag key:value pairs that identify this series within a group-by
  name: group_tags
  type: array
- description: The numeric values at each timestamp
  name: values
  type: array
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-metrics-timeseries-result-schema.json
slug: datadog-metrics-timeseries-result
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: TimeseriesResult
---
