---
description: An action to be performed when the <code>condition</code> is TRUE.
layout: schema
name: Action
properties_list:
- description: ''
  name: setVariable
  type: object
- description: ''
  name: sns
  type: object
- description: ''
  name: iotTopicPublish
  type: object
- description: ''
  name: setTimer
  type: object
- description: ''
  name: clearTimer
  type: object
- description: ''
  name: resetTimer
  type: object
- description: ''
  name: lambda
  type: object
- description: ''
  name: iotEvents
  type: object
- description: ''
  name: sqs
  type: object
- description: ''
  name: firehose
  type: object
- description: ''
  name: dynamoDB
  type: object
- description: ''
  name: dynamoDBv2
  type: object
- description: ''
  name: iotSiteWise
  type: object
provider_name: Amazon IoT Events
provider_slug: amazon-iot-events
schema_file: json-schema/iot-events-action-schema.json
slug: iot-events-action
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
title: Action
---
