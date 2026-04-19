---
description: Represents a CloudWatch metric alarm
layout: schema
name: Alarm
properties_list:
- description: The name of the alarm
  name: alarmName
  type: string
- description: The ARN of the alarm
  name: alarmArn
  type: string
- description: The description of the alarm
  name: alarmDescription
  type: string
- description: The state value for the alarm
  name: stateValue
  type: string
- description: An explanation for the alarm state
  name: stateReason
  type: string
- description: The time stamp of the last update to the state
  name: stateUpdatedTimestamp
  type: string
- description: The name of the metric associated with the alarm
  name: metricName
  type: string
- description: The namespace of the metric associated with the alarm
  name: namespace
  type: string
- description: The statistic for the metric associated with the alarm
  name: statistic
  type: string
- description: The dimensions for the metric associated with the alarm
  name: dimensions
  type: array
- description: The period in seconds over which the statistic is applied
  name: period
  type: integer
- description: The number of periods over which data is compared to the threshold
  name: evaluationPeriods
  type: integer
- description: The value to compare with the specified statistic
  name: threshold
  type: number
- description: The arithmetic operation to use when comparing the statistic and threshold
  name: comparisonOperator
  type: string
- description: How missing data points are treated
  name: treatMissingData
  type: string
- description: Whether actions are executed during alarm state changes
  name: actionsEnabled
  type: boolean
- description: The actions to execute when the alarm transitions to ALARM state
  name: alarmActions
  type: array
- description: The actions to execute when the alarm transitions to OK state
  name: okActions
  type: array
- description: The actions to execute when the alarm transitions to INSUFFICIENT_DATA state
  name: insufficientDataActions
  type: array
provider_name: Amazon CloudWatch
provider_slug: amazon-cloudwatch
schema_file: json-schema/cloudwatch-alarm-schema.json
slug: cloudwatch-alarm
tags:
- AWS
- CloudWatch
- Monitoring
- Observability
- Metrics
- Logs
title: Alarm
---
