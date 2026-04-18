---
description: Request body for aggregating log events
layout: schema
name: LogsAggregateRequest
properties_list:
- description: ''
  name: filter
  type: object
- description: List of aggregation computations to perform on the filtered log set
  name: compute
  type: array
- description: List of facets to group results by, enabling breakdown by log attribute
  name: group_by
  type: array
- description: Options for the aggregation query
  name: options
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-logs-aggregate-request-schema.json
slug: datadog-logs-logs-aggregate-request
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: LogsAggregateRequest
---
