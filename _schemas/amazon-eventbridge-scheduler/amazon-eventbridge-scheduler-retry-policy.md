---
description: A <code>RetryPolicy</code> object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.
layout: schema
name: RetryPolicy
properties_list:
- description: ''
  name: MaximumEventAgeInSeconds
  type: object
- description: ''
  name: MaximumRetryAttempts
  type: object
provider_name: Amazon EventBridge Scheduler
provider_slug: amazon-eventbridge-scheduler
schema_file: json-schema/amazon-eventbridge-scheduler-retry-policy-schema.json
slug: amazon-eventbridge-scheduler-retry-policy
tags:
- Amazon Web Services
- AWS
- Cron
- Event-Driven
- Scheduling
- Serverless
title: RetryPolicy
---
