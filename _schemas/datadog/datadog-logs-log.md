---
description: A single log event returned from a search query
layout: schema
name: Log
properties_list:
- description: The unique identifier of the log event
  name: id
  type: string
- description: The type of the resource (always 'log')
  name: type
  type: string
- description: ''
  name: attributes
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-log-schema.json
slug: datadog-logs-log
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Log
---
