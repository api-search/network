---
description: Rule schema from Amazon EventBridge API
layout: schema
name: Rule
properties_list:
- description: The name of the rule.
  name: Name
  type: string
- description: The Amazon Resource Name (ARN) of the rule.
  name: Arn
  type: string
- description: The event pattern of the rule.
  name: EventPattern
  type: string
- description: The state of the rule.
  name: State
  type: string
- description: The description of the rule.
  name: Description
  type: string
- description: The scheduling expression (e.g., cron or rate expression).
  name: ScheduleExpression
  type: string
- description: The Amazon Resource Name (ARN) of the IAM role.
  name: RoleArn
  type: string
- description: The name or ARN of the event bus associated with the rule.
  name: EventBusName
  type: string
provider_name: Amazon EventBridge
provider_slug: amazon-eventbridge
schema_file: json-schema/amazon-eventbridge-rule-schema.json
slug: amazon-eventbridge-rule
tags:
- Amazon Web Services
- AWS
- Event Bus
- Event-Driven
- Events
- Integration
- Serverless
title: Rule
---
