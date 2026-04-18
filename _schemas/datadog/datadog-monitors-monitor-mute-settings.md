---
description: Settings for muting a monitor including scope and expiration
layout: schema
name: MonitorMuteSettings
properties_list:
- description: The scope expression specifying which monitor groups to mute (e.g., env:prod, host:web-01)
  name: scope
  type: string
- description: Unix timestamp in seconds when the mute expires; omit for indefinite mute
  name: end
  type: integer
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-monitors-monitor-mute-settings-schema.json
slug: datadog-monitors-monitor-mute-settings
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MonitorMuteSettings
---
