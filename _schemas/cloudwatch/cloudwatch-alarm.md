---
description: Schema for an Amazon CloudWatch alarm resource, representing a watch over a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. The alarm triggers actions when the metric or expression value breaches a defined threshold over a specified number of evaluation periods.
layout: schema
name: Amazon CloudWatch Alarm
properties_list:
- description: The name of the alarm. This name must be unique within the Region and within the AWS account. The maximum length is 255 characters.
  name: AlarmName
  type: string
- description: The Amazon Resource Name (ARN) of the alarm, in the format arn:aws:cloudwatch:region:account-id:alarm:alarm-name.
  name: AlarmArn
  type: string
- description: The description for the alarm. Up to 1024 characters.
  name: AlarmDescription
  type: string
- description: The time stamp of the last update to the alarm configuration, in ISO 8601 format.
  name: AlarmConfigurationUpdatedTimestamp
  type: string
- description: Indicates whether actions should be executed during any changes to the alarm state. When set to false, the alarm state changes but no actions are executed.
  name: ActionsEnabled
  type: boolean
- description: The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an ARN. A maximum of 5 actions are allowed.
  name: OKActions
  type: array
- description: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an ARN. A maximum of 5 actions are allowed.
  name: AlarmActions
  type: array
- description: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an ARN. A maximum of 5 actions are allowed.
  name: InsufficientDataActions
  type: array
- description: The current state value for the alarm. OK indicates the metric or expression is within the defined threshold. ALARM indicates the metric or expression is outside of the defined threshold. INSUFFICIENT
  name: StateValue
  type: string
- description: An explanation for the alarm state, in text format. Provides a human-readable explanation of why the alarm is in its current state.
  name: StateReason
  type: string
- description: An explanation for the alarm state, in JSON format. Contains machine-readable data about the evaluation that led to the current alarm state.
  name: StateReasonData
  type: string
- description: The time stamp of the last update to the alarm's StateValue or StateReasonData, in ISO 8601 format.
  name: StateUpdatedTimestamp
  type: string
- description: The date and time that the alarm's StateValue most recently changed, in ISO 8601 format.
  name: StateTransitionedTimestamp
  type: string
- description: The name of the metric associated with the alarm, if this is a single-metric alarm.
  name: MetricName
  type: string
- description: The namespace of the metric associated with the alarm. Namespaces that begin with AWS/ are reserved for AWS services.
  name: Namespace
  type: string
- description: The statistic for the metric specified in MetricName, other than percentile.
  name: Statistic
  type: string
- description: The percentile statistic for the metric specified in MetricName. Specify a value between p0.0 and p100.
  name: ExtendedStatistic
  type: string
- description: The dimensions for the metric specified in MetricName. A maximum of 30 dimensions are allowed per metric.
  name: Dimensions
  type: array
- description: The length, in seconds, used each time the metric specified in MetricName is evaluated. Valid values are 10, 30, and any multiple of 60. For high-resolution metrics, the period can be 10 or 30 seconds
  name: Period
  type: integer
- description: The unit of measure for the statistic. If you do not specify Unit, CloudWatch retrieves all unit types that have been published for the metric.
  name: Unit
  type: string
- description: The number of periods over which data is compared to the specified threshold. An alarm is triggered only if enough periods breach the threshold according to DatapointsToAlarm.
  name: EvaluationPeriods
  type: integer
- description: The number of data points that must be breaching to trigger the alarm. This is used only if you are setting an M out of N alarm. The value must be less than or equal to EvaluationPeriods.
  name: DatapointsToAlarm
  type: integer
- description: The value against which the specified statistic is compared. This value is used with ComparisonOperator to determine if the alarm should transition to the ALARM state.
  name: Threshold
  type: number
- description: The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand. The anomaly-detection-specific operators are used with
  name: ComparisonOperator
  type: string
- description: Sets how this alarm is to handle missing data points. breaching treats missing data as breaching the threshold. notBreaching treats missing data as being within the threshold. ignore maintains the cur
  name: TreatMissingData
  type: string
- description: Used only for alarms based on percentile statistics. If ignore, the alarm state does not change during periods with too few data points to be statistically significant.
  name: EvaluateLowSampleCountPercentile
  type: string
- description: An array of MetricDataQuery structures indicating the metrics to be returned and the math expressions to perform. Used for metric math expression-based alarms.
  name: Metrics
  type: array
- description: If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.
  name: ThresholdMetricId
  type: string
- description: A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm.
  name: Tags
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-alarm-schema.json
slug: cloudwatch-alarm
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: Amazon CloudWatch Alarm
---
