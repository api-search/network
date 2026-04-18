---
description: A Datadog monitor that watches a metric or check and alerts when thresholds are exceeded
layout: schema
name: Monitor
properties_list:
- description: The unique numeric identifier of the monitor, assigned by Datadog upon creation
  name: id
  type: integer
- description: The type of monitor that determines the query language and alerting behavior
  name: type
  type: string
- description: The monitor query expression using Datadog's query language for the specified monitor type
  name: query
  type: string
- description: A descriptive name for the monitor used for identification in dashboards and notifications
  name: name
  type: string
- description: The notification message body sent when the monitor triggers, supports template variables and @-mentions
  name: message
  type: string
- description: List of tags to associate with the monitor for filtering and organization
  name: tags
  type: array
- description: ''
  name: options
  type: object
- description: The monitor priority level from 1 (highest) to 5 (lowest), used for sorting and filtering
  name: priority
  type: integer
- description: ''
  name: state
  type: object
- description: ''
  name: creator
  type: object
- description: ISO 8601 timestamp when the monitor was created
  name: created
  type: string
- description: ISO 8601 timestamp when the monitor was last modified
  name: modified
  type: string
- description: ISO 8601 timestamp when the monitor was deleted, or null if not deleted
  name: deleted
  type: string
- description: List of role IDs whose members can edit this monitor; empty means all users can edit
  name: restricted_roles
  type: array
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitors-monitor-schema.json
slug: datadog-monitors-monitor
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Monitor
---
