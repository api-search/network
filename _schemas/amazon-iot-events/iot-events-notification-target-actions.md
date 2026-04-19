---
description: Specifies an AWS Lambda function to manage alarm notifications. You can create one or use the <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html">AWS Lambda function provided by AWS IoT Events</a>.
layout: schema
name: NotificationTargetActions
properties_list:
- description: Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.
  name: lambdaAction
  type: object
provider_name: Amazon IoT Events
provider_slug: amazon-iot-events
schema_file: json-schema/iot-events-notification-target-actions-schema.json
slug: iot-events-notification-target-actions
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
title: NotificationTargetActions
---
