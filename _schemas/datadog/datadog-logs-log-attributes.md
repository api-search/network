---
description: The attributes of a log event returned from the search API
layout: schema
name: LogAttributes
properties_list:
- description: ISO 8601 timestamp when the log was generated
  name: timestamp
  type: string
- description: The log level or severity status of the event
  name: status
  type: string
- description: The raw log message content
  name: message
  type: string
- description: The hostname of the machine that generated the log
  name: host
  type: string
- description: The name of the application or service that generated the log
  name: service
  type: string
- description: The technology source that generated the log (e.g., nginx, java)
  name: source
  type: string
- description: List of tags associated with the log event in key:value format
  name: tags
  type: array
- description: Custom key-value attributes extracted from the log message
  name: attributes
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-log-attributes-schema.json
slug: datadog-logs-log-attributes
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: LogAttributes
---
