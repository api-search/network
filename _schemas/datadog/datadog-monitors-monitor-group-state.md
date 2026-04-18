---
description: The state of a single monitor group (a unique combination of tag values)
layout: schema
name: MonitorGroupState
properties_list:
- description: The current alert status for this monitor group
  name: status
  type: string
- description: The name of the monitor group, represented as a comma-separated list of tag:value pairs
  name: name
  type: string
- description: Unix timestamp in seconds of the last time this group triggered an alert
  name: last_triggered_ts
  type: integer
- description: Unix timestamp in seconds of the last time a notification was sent for this group
  name: last_notified_ts
  type: integer
- description: Unix timestamp in seconds of the last time this group resolved from an alert state
  name: last_resolved_ts
  type: integer
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitors-monitor-group-state-schema.json
slug: datadog-monitors-monitor-group-state
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MonitorGroupState
---
