---
description: Target schema from Amazon EventBridge API
layout: schema
name: Target
properties_list:
- description: The ID of the target.
  name: Id
  type: string
- description: The Amazon Resource Name (ARN) of the target.
  name: Arn
  type: string
- description: The Amazon Resource Name (ARN) of the IAM role.
  name: RoleArn
  type: string
- description: Valid JSON text passed to the target.
  name: Input
  type: string
- description: JSONPath to extract from the event and send to the target.
  name: InputPath
  type: string
- description: Settings to transform input before sending to the target.
  name: InputTransformer
  type: object
provider_name: Amazon EventBridge
provider_slug: amazon-eventbridge
schema_file: json-schema/amazon-eventbridge-target-schema.json
slug: amazon-eventbridge-target
tags:
- Amazon Web Services
- AWS
- Event Bus
- Event-Driven
- Events
- Integration
- Serverless
title: Target
---
