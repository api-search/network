---
description: Represents an Amazon CloudWatch metric alarm with its associated configuration, state, and notification actions.
layout: schema
name: Amazon CloudWatch Alarm
properties_list:
- description: The name of the alarm
  name: alarmName
  type: string
- description: The Amazon Resource Name (ARN) of the alarm
  name: alarmArn
  type: string
- description: The description for the alarm
  name: alarmDescription
  type: string
- description: The time stamp of the last update to the alarm configuration
  name: alarmConfigurationUpdatedTimestamp
  type: string
- description: Indicates whether actions should be executed during any changes to the alarm state
  name: actionsEnabled
  type: boolean
- description: The actions to execute when this alarm transitions to the ALARM state
  name: alarmActions
  type: array
- description: The actions to execute when this alarm transitions to the OK state
  name: okActions
  type: array
- description: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state
  name: insufficientDataActions
  type: array
- description: The state value for the alarm
  name: stateValue
  type: string
- description: An explanation for the alarm state in human-readable text format
  name: stateReason
  type: string
- description: An explanation for the alarm state in JSON format
  name: stateReasonData
  type: string
- description: The time stamp of the last update to the alarm state
  name: stateUpdatedTimestamp
  type: string
- description: The name of the metric associated with the alarm
  name: metricName
  type: string
- description: The namespace of the metric associated with the alarm
  name: namespace
  type: string
- description: The statistic for the metric specified in MetricName
  name: statistic
  type: string
- description: The percentile statistic for the metric specified in MetricName
  name: extendedStatistic
  type: string
- description: The dimensions for the metric specified in MetricName
  name: dimensions
  type: array
- description: The length in seconds of the evaluation period for the alarm
  name: period
  type: integer
- description: The number of periods over which data is compared to the specified threshold
  name: evaluationPeriods
  type: integer
- description: The number of data points that must be breaching to trigger the alarm
  name: datapointsToAlarm
  type: integer
- description: The value against which the specified statistic is compared
  name: threshold
  type: number
- description: The arithmetic operation to use when comparing the specified statistic and threshold
  name: comparisonOperator
  type: string
- description: Sets how this alarm is to handle missing data points
  name: treatMissingData
  type: string
- description: The unit of measure for the statistic
  name: unit
  type: string
- description: Tags associated with the alarm
  name: tags
  type: array
provider_name: Amazon CloudWatch
provider_slug: amazon-cloudwatch
schema_file: json-schema/amazon-cloudwatch-alarm-schema.json
slug: amazon-cloudwatch-alarm
tags:
- AWS
- CloudWatch
- Monitoring
- Observability
- Metrics
- Logs
title: Amazon CloudWatch Alarm
---
