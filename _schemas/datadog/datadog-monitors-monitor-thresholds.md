---
description: Alert threshold values for metric and service check monitors
layout: schema
name: MonitorThresholds
properties_list:
- description: The threshold value that triggers a CRITICAL alert notification
  name: critical
  type: number
- description: The threshold value at which a CRITICAL alert recovers to OK state
  name: critical_recovery
  type: number
- description: The threshold value that triggers a WARNING alert notification
  name: warning
  type: number
- description: The threshold value at which a WARNING alert recovers to OK state
  name: warning_recovery
  type: number
- description: The threshold for service check monitors indicating an OK state (used with service check monitors)
  name: ok
  type: number
- description: The threshold for service check monitors indicating an UNKNOWN state
  name: unknown
  type: number
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitors-monitor-thresholds-schema.json
slug: datadog-monitors-monitor-thresholds
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MonitorThresholds
---
