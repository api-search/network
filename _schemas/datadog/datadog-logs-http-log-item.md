---
description: A single log entry to submit to Datadog
layout: schema
name: HTTPLogItem
properties_list:
- description: The message content of the log entry. This field is required and indexed for search.
  name: message
  type: string
- description: The name of the host that generated the log entry
  name: hostname
  type: string
- description: The name of the application or service that generated the log
  name: service
  type: string
- description: The source technology of the log (e.g., nginx, redis, java) used for automatic processing
  name: ddsource
  type: string
- description: Comma-separated list of tags to apply to the log entry in key:value format
  name: ddtags
  type: string
- description: The severity or log level of the event (e.g., info, warning, error, critical)
  name: status
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-http-log-item-schema.json
slug: datadog-logs-http-log-item
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: HTTPLogItem
---
