---
description: The details about a composite alarm.
layout: schema
name: CompositeAlarm
properties_list:
- description: Indicates whether actions should be executed during changes to the alarm state.
  name: ActionsEnabled
  type: boolean
- description: The actions to execute when this alarm transitions to the ALARM state.
  name: AlarmActions
  type: array
- description: The Amazon Resource Name (ARN) of the alarm.
  name: AlarmArn
  type: string
- description: The time stamp of the last update to the alarm configuration.
  name: AlarmConfigurationUpdatedTimestamp
  type: string
- description: The description of the alarm.
  name: AlarmDescription
  type: string
- description: The name of the alarm.
  name: AlarmName
  type: string
- description: The rule that this alarm uses to evaluate its alarm state.
  name: AlarmRule
  type: string
- description: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state.
  name: InsufficientDataActions
  type: array
- description: The actions to execute when this alarm transitions to the OK state.
  name: OKActions
  type: array
- description: An explanation for the alarm state, in text format.
  name: StateReason
  type: string
- description: An explanation for the alarm state, in JSON format.
  name: StateReasonData
  type: string
- description: The timestamp of the last change to the alarm's StateValue.
  name: StateUpdatedTimestamp
  type: string
- description: The timestamp of the last state transition.
  name: StateTransitionedTimestamp
  type: string
- description: When the value is ALARM, it means that the actions are suppressed.
  name: ActionsSuppressedBy
  type: string
- description: Describes why the actions are suppressed.
  name: ActionsSuppressedReason
  type: string
- description: The ARN of the alarm used as the actions suppressor.
  name: ActionsSuppressor
  type: string
- description: The maximum time in seconds that the composite alarm waits after suppressor alarm goes into ALARM state.
  name: ActionsSuppressorWaitPeriod
  type: integer
- description: The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of ALARM state.
  name: ActionsSuppressorExtensionPeriod
  type: integer
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-composite-alarm-schema.json
slug: cloudwatch-composite-alarm
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: CompositeAlarm
---
