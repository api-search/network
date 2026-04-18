---
description: A log event stored in Datadog Log Management. Log events represent individual log entries collected from applications, infrastructure, cloud services, and custom sources. Each log event has a unique identifier, a timestamp, a message, and optional structured attributes extracted from the log content. Logs are indexed and searchable using Datadog's log query language and can be correlated with metrics, traces, and events for full observability.
layout: schema
name: Datadog Log Event
properties_list:
- description: The unique string identifier assigned by Datadog to this log event. The ID is generated at ingestion time and can be used to retrieve a specific log event via the API or Logs Explorer.
  name: id
  type: string
- description: The resource type identifier for log events returned by the Datadog API (always 'log')
  name: type
  type: string
- description: ''
  name: content
  type: object
- description: ''
  name: attributes
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-log-event-schema.json
slug: datadog-log-event
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Datadog Log Event
---
