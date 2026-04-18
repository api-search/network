---
description: Configuration options for a monitor controlling evaluation, notification, and recovery behavior
layout: schema
name: MonitorOptions
properties_list:
- description: ''
  name: thresholds
  type: object
- description: Whether to send a notification when there is no data for the monitored metric
  name: notify_no_data
  type: boolean
- description: The number of minutes after which the monitor reports no data (minimum 2x the evaluation timeframe)
  name: no_data_timeframe
  type: integer
- description: Whether the monitor requires a full evaluation window of data before alerting
  name: require_full_window
  type: boolean
- description: Whether to send notifications to auditors when the monitor is changed
  name: notify_audit
  type: boolean
- description: The number of minutes between re-notifications while the monitor remains in an alert state (0 to disable)
  name: renotify_interval
  type: integer
- description: Monitor status types that trigger re-notification messages
  name: renotify_statuses
  type: array
- description: The message to include with re-notification alerts instead of the main message
  name: escalation_message
  type: string
- description: The number of hours after which an automatically resolving alert times out
  name: timeout_h
  type: integer
- description: The time in seconds to delay evaluation, used to ensure all data arrives before checking thresholds
  name: evaluation_delay
  type: integer
- description: The number of seconds to delay notification for new monitor groups to allow transient issues to resolve
  name: new_group_delay
  type: integer
- description: Whether to include group scope tags in notification subject and body
  name: include_tags
  type: boolean
- description: Map of monitor scopes to Unix timestamps indicating when each scope's mute expires (0 for indefinite)
  name: silenced
  type: object
- description: Aggregation settings used for anomaly and outlier monitors
  name: aggregation
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitors-monitor-options-schema.json
slug: datadog-monitors-monitor-options
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MonitorOptions
---
