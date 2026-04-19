---
description: The schedule's target. EventBridge Scheduler supports templated target that invoke common API operations, as well as universal targets that you can customize to invoke over 6,000 API operations across more than 270 services. You can only specify one templated or universal target for a schedule.
layout: schema
name: Target
properties_list:
- description: ''
  name: Arn
  type: object
- description: ''
  name: DeadLetterConfig
  type: object
- description: ''
  name: EcsParameters
  type: object
- description: ''
  name: EventBridgeParameters
  type: object
- description: ''
  name: Input
  type: object
- description: ''
  name: KinesisParameters
  type: object
- description: ''
  name: RetryPolicy
  type: object
- description: ''
  name: RoleArn
  type: object
- description: ''
  name: SageMakerPipelineParameters
  type: object
- description: ''
  name: SqsParameters
  type: object
provider_name: Amazon EventBridge Scheduler
provider_slug: amazon-eventbridge-scheduler
schema_file: json-schema/amazon-eventbridge-scheduler-target-schema.json
slug: amazon-eventbridge-scheduler-target
tags:
- Amazon Web Services
- AWS
- Cron
- Event-Driven
- Scheduling
- Serverless
title: Target
---
