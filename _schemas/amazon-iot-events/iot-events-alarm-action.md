---
description: Specifies one of the following actions to receive notifications when the alarm state changes.
layout: schema
name: AlarmAction
properties_list:
- description: Information required to publish the Amazon SNS message.
  name: sns
  type: object
- description: Information required to publish the MQTT message through the AWS IoT message broker.
  name: iotTopicPublish
  type: object
- description: Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.
  name: lambda
  type: object
- description: Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.
  name: iotEvents
  type: object
- description: Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.
  name: sqs
  type: object
- description: Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.
  name: firehose
  type: object
- description: <p>Defines an action to write to the Amazon DynamoDB table that you created. The standard action payload contains all the information about the detector model instance and the event that triggered the
  name: dynamoDB
  type: object
- description: '<p>Defines an action to write to the Amazon DynamoDB table that you created. The default action payload contains all the information about the detector model instance and the event that triggered the '
  name: dynamoDBv2
  type: object
- description: '<p>Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise.</p> <p>You must use expressions for all parameters in '
  name: iotSiteWise
  type: object
provider_name: Amazon IoT Events
provider_slug: amazon-iot-events
schema_file: json-schema/iot-events-alarm-action-schema.json
slug: iot-events-alarm-action
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
title: AlarmAction
---
