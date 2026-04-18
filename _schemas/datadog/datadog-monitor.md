---
description: A Datadog monitor that continuously evaluates a query against defined thresholds and sends notifications when alert conditions are triggered. Monitors are the foundation of Datadog's alerting system and support metric thresholds, anomaly detection, outlier detection, log patterns, APM traces, synthetic test results, and composite conditions. Each monitor tracks the status of one or more groups defined by the query's group-by tags.
layout: schema
name: Datadog Monitor
properties_list:
- description: The unique numeric identifier assigned by Datadog when the monitor is created. Read-only and used to reference the monitor in API calls and URLs.
  name: id
  type: integer
- description: The type of monitor which determines the query language, threshold options, and evaluation behavior. The most common type is 'metric alert' for threshold-based alerting on metrics.
  name: type
  type: string
- description: The monitor query expression defining what to evaluate and when to alert. The query syntax depends on the monitor type. For metric alerts, uses Datadog's metrics query language with threshold conditio
  name: query
  type: string
- description: A descriptive name for the monitor shown in the Monitors list, notification subject lines, and dashboard widgets. Should clearly describe what is being monitored and what constitutes an alert conditio
  name: name
  type: string
- description: The notification message body sent to alert recipients when the monitor triggers. Supports Datadog template variables (e.g., {{host.name}}, {{value}}), conditional blocks, and @-mentions for routing n
  name: message
  type: string
- description: List of tags to associate with the monitor for organization, filtering, and scoping. Tags appear in the Monitors list and can be used to group monitors by team, service, or environment. Tags do not af
  name: tags
  type: array
- description: ''
  name: options
  type: object
- description: The monitor priority level from 1 (highest/most critical) to 5 (lowest). Priority is used for sorting monitors in the Monitors list and can be used to filter monitors in notification rules.
  name: priority
  type: integer
- description: ''
  name: state
  type: object
- description: ''
  name: creator
  type: object
- description: ISO 8601 timestamp when the monitor was created. Set automatically by Datadog and cannot be modified.
  name: created
  type: string
- description: ISO 8601 timestamp when the monitor was last modified. Updated automatically whenever the monitor configuration is changed.
  name: modified
  type: string
- description: ISO 8601 timestamp when the monitor was soft-deleted, or null if the monitor is active. Soft-deleted monitors are hidden but retained for a period before permanent deletion.
  name: deleted
  type:
  - string
  - 'null'
- description: List of role IDs whose members are allowed to edit this monitor. When set, only users with at least one of the specified roles can modify the monitor. An empty array means all users with monitor write
  name: restricted_roles
  type: array
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitor-schema.json
slug: datadog-monitor
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Datadog Monitor
---
