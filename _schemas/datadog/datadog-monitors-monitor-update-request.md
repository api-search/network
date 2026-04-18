---
description: Request body for updating an existing monitor configuration
layout: schema
name: MonitorUpdateRequest
properties_list:
- description: The type of the monitor (changing type may reset other settings)
  name: type
  type: string
- description: The updated monitor query expression
  name: query
  type: string
- description: The updated descriptive name for the monitor
  name: name
  type: string
- description: The updated notification message body
  name: message
  type: string
- description: The updated list of tags to associate with the monitor
  name: tags
  type: array
- description: ''
  name: options
  type: object
- description: The updated priority level (1 highest to 5 lowest)
  name: priority
  type: integer
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitors-monitor-update-request-schema.json
slug: datadog-monitors-monitor-update-request
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MonitorUpdateRequest
---
