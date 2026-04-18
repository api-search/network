---
description: Response containing matching log events from a search query
layout: schema
name: LogsListResponse
properties_list:
- description: List of matching log events
  name: data
  type: array
- description: Metadata about the search response including pagination information
  name: meta
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-logs-list-response-schema.json
slug: datadog-logs-logs-list-response
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: LogsListResponse
---
