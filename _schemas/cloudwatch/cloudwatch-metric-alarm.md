---
description: The details about a metric alarm.
layout: schema
name: MetricAlarm
properties_list:
- description: The name of the alarm.
  name: AlarmName
  type: string
- description: The Amazon Resource Name (ARN) of the alarm.
  name: AlarmArn
  type: string
- description: The description of the alarm.
  name: AlarmDescription
  type: string
- description: The time stamp of the last update to the alarm configuration.
  name: AlarmConfigurationUpdatedTimestamp
  type: string
- description: Indicates whether actions should be executed during any changes to the alarm state.
  name: ActionsEnabled
  type: boolean
- description: The actions to execute when this alarm transitions to the OK state.
  name: OKActions
  type: array
- description: The actions to execute when this alarm transitions to the ALARM state.
  name: AlarmActions
  type: array
- description: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state.
  name: InsufficientDataActions
  type: array
- description: An explanation for the alarm state, in text format.
  name: StateReason
  type: string
- description: An explanation for the alarm state, in JSON format.
  name: StateReasonData
  type: string
- description: The time stamp of the last update to the value of either the StateValue or StateReasonData.
  name: StateUpdatedTimestamp
  type: string
- description: The name of the metric associated with the alarm.
  name: MetricName
  type: string
- description: The namespace of the metric associated with the alarm.
  name: Namespace
  type: string
- description: The percentile statistic for the metric associated with the alarm.
  name: ExtendedStatistic
  type: string
- description: The dimensions for the metric associated with the alarm.
  name: Dimensions
  type: array
- description: The period, in seconds, over which the statistic is applied.
  name: Period
  type: integer
- description: The number of periods over which data is compared to the specified threshold.
  name: EvaluationPeriods
  type: integer
- description: The number of data points that must be breaching to trigger the alarm.
  name: DatapointsToAlarm
  type: integer
- description: The value to compare with the specified statistic.
  name: Threshold
  type: number
- description: Sets how this alarm is to handle missing data points.
  name: TreatMissingData
  type: string
- description: Used only for alarms based on percentiles.
  name: EvaluateLowSampleCountPercentile
  type: string
- description: An array of MetricDataQuery structures for metric math expressions.
  name: Metrics
  type: array
- description: If the value of this field is set to an alarm metric ID, the alarm is based on an anomaly detection model.
  name: ThresholdMetricId
  type: string
- description: The date and time that the alarm's StateValue most recently changed.
  name: StateTransitionedTimestamp
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-alarm-schema.json
slug: cloudwatch-metric-alarm
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricAlarm
---
