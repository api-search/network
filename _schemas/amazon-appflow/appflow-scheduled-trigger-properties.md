---
description: ScheduledTriggerProperties schema from Amazon AppFlow API
layout: schema
name: ScheduledTriggerProperties
properties_list:
- description: The scheduling expression that determines the rate at which the schedule will run, for example rate(5minutes).
  name: scheduleExpression
  type: string
- description: Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
  name: dataPullMode
  type: string
- description: The time at which the scheduled flow starts.
  name: scheduleStartTime
  type: integer
- description: The time at which the scheduled flow ends.
  name: scheduleEndTime
  type: integer
- description: Specifies the time zone used when referring to the date and time of a scheduled-triggered flow.
  name: timezone
  type: string
- description: Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
  name: scheduleOffset
  type: integer
- description: Specifies the date range for the records to import from the connector in the first flow run.
  name: firstExecutionFrom
  type: integer
- description: Defines how many times a scheduled flow fails consecutively before Amazon AppFlow deactivates it.
  name: flowErrorDeactivationThreshold
  type: integer
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-scheduled-trigger-properties-schema.json
slug: appflow-scheduled-trigger-properties
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: ScheduledTriggerProperties
---
