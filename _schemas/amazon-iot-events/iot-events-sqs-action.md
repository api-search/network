---
description: Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.
layout: schema
name: SqsAction
properties_list:
- description: ''
  name: queueUrl
  type: object
- description: ''
  name: useBase64
  type: object
- description: ''
  name: payload
  type: object
provider_name: Amazon IoT Events
provider_slug: amazon-iot-events
schema_file: json-schema/iot-events-sqs-action-schema.json
slug: iot-events-sqs-action
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
title: SqsAction
---
