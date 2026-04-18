---
description: Request body for searching log events
layout: schema
name: LogsListRequest
properties_list:
- description: ''
  name: filter
  type: object
- description: The sort order for log results, either ascending or descending by timestamp
  name: sort
  type: string
- description: Pagination configuration for log search results
  name: page
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-logs-list-request-schema.json
slug: datadog-logs-logs-list-request
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: LogsListRequest
---
