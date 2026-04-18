---
description: ''
layout: schema
name: DescribeAlarmHistoryInput
properties_list:
- description: The name of the alarm.
  name: AlarmName
  type: string
- description: Specify this parameter to receive information only about alarms of the specified types.
  name: AlarmTypes
  type: array
- description: The type of alarm histories to retrieve.
  name: HistoryItemType
  type: string
- description: The starting date to retrieve alarm history.
  name: StartDate
  type: string
- description: The ending date to retrieve alarm history.
  name: EndDate
  type: string
- description: The maximum number of alarm history records to retrieve.
  name: MaxRecords
  type: integer
- description: The token returned by a previous call.
  name: NextToken
  type: string
- description: Specified whether to return the newest or oldest alarm history first.
  name: ScanBy
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-describe-alarm-history-input-schema.json
slug: cloudwatch-describe-alarm-history-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DescribeAlarmHistoryInput
---
