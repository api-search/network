---
description: ''
layout: schema
name: SetAlarmStateInput
properties_list:
- description: The name of the alarm.
  name: AlarmName
  type: string
- description: The reason that this alarm is set to this specific state, in text format.
  name: StateReason
  type: string
- description: The reason that this alarm is set to this specific state, in JSON format.
  name: StateReasonData
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-set-alarm-state-input-schema.json
slug: cloudwatch-set-alarm-state-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: SetAlarmStateInput
---
