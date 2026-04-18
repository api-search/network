---
description: Filter criteria for log search queries
layout: schema
name: LogsQueryFilter
properties_list:
- description: A Datadog log search query string to filter log events (e.g., service:web status:error)
  name: query
  type: string
- description: List of log index names to search; if empty, all indexes are searched
  name: indexes
  type: array
- description: The start of the time range for the search in ISO 8601 format or relative format (e.g., now-15m)
  name: from
  type: string
- description: The end of the time range for the search in ISO 8601 format or relative format (e.g., now)
  name: to
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-logs-query-filter-schema.json
slug: datadog-logs-logs-query-filter
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: LogsQueryFilter
---
