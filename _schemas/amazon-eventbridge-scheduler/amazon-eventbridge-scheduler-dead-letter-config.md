---
description: An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.
layout: schema
name: DeadLetterConfig
properties_list:
- description: ''
  name: Arn
  type: object
provider_name: Amazon EventBridge Scheduler
provider_slug: amazon-eventbridge-scheduler
schema_file: json-schema/amazon-eventbridge-scheduler-dead-letter-config-schema.json
slug: amazon-eventbridge-scheduler-dead-letter-config
tags:
- Amazon Web Services
- AWS
- Cron
- Event-Driven
- Scheduling
- Serverless
title: DeadLetterConfig
---
