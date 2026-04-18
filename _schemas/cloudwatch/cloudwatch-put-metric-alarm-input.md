---
description: ''
layout: schema
name: PutMetricAlarmInput
properties_list:
- description: The name for the alarm.
  name: AlarmName
  type: string
- description: The description for the alarm.
  name: AlarmDescription
  type: string
- description: Indicates whether actions should be executed during any changes to the alarm state.
  name: ActionsEnabled
  type: boolean
- description: The actions to execute when this alarm transitions to an OK state.
  name: OKActions
  type: array
- description: The actions to execute when this alarm transitions to the ALARM state.
  name: AlarmActions
  type: array
- description: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state.
  name: InsufficientDataActions
  type: array
- description: The name for the metric associated with the alarm.
  name: MetricName
  type: string
- description: The namespace for the metric associated with the alarm.
  name: Namespace
  type: string
- description: The percentile statistic for the metric specified in MetricName.
  name: ExtendedStatistic
  type: string
- description: The dimensions for the metric specified in MetricName.
  name: Dimensions
  type: array
- description: The length, in seconds, used each time the metric specified in MetricName is evaluated.
  name: Period
  type: integer
- description: The number of periods over which data is compared to the specified threshold.
  name: EvaluationPeriods
  type: integer
- description: The number of data points that must be breaching to trigger the alarm.
  name: DatapointsToAlarm
  type: integer
- description: The value against which the specified statistic is compared.
  name: Threshold
  type: number
- description: Sets how this alarm is to handle missing data points.
  name: TreatMissingData
  type: string
- description: Used only for alarms based on percentiles.
  name: EvaluateLowSampleCountPercentile
  type: string
- description: An array of MetricDataQuery structures for metric math expression alarms.
  name: Metrics
  type: array
- description: A list of key-value pairs to associate with the alarm.
  name: Tags
  type: array
- description: If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.
  name: ThresholdMetricId
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-put-metric-alarm-input-schema.json
slug: cloudwatch-put-metric-alarm-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: PutMetricAlarmInput
---
