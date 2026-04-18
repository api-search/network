---
description: Settings for unmuting a monitor including optional scope
layout: schema
name: MonitorUnmuteSettings
properties_list:
- description: The scope expression specifying which monitor groups to unmute; omit to unmute all groups
  name: scope
  type: string
- description: When true, unmutes all scopes including those previously muted with different scope expressions
  name: all_scopes
  type: boolean
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitors-monitor-unmute-settings-schema.json
slug: datadog-monitors-monitor-unmute-settings
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MonitorUnmuteSettings
---
