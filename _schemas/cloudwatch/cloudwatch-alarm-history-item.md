---
description: Represents the history of a specific alarm.
layout: schema
name: AlarmHistoryItem
properties_list:
- description: The descriptive name for the alarm.
  name: AlarmName
  type: string
- description: The type of alarm, either metric alarm or composite alarm.
  name: AlarmType
  type: string
- description: The time stamp for the alarm history item.
  name: Timestamp
  type: string
- description: The type of alarm history item.
  name: HistoryItemType
  type: string
- description: A summary of the alarm history, in text format.
  name: HistorySummary
  type: string
- description: Data about the alarm, in JSON format.
  name: HistoryData
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-alarm-history-item-schema.json
slug: cloudwatch-alarm-history-item
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: AlarmHistoryItem
---
