---
description: ''
layout: schema
name: TaskDef
properties_list:
- description: The name of the task definition
  name: name
  type: string
- description: Description of the task
  name: description
  type: string
- description: Number of retries
  name: retryCount
  type: integer
- description: Retry logic
  name: retryLogic
  type: string
- description: Delay between retries in seconds
  name: retryDelaySeconds
  type: integer
- description: Task execution timeout in seconds
  name: timeoutSeconds
  type: integer
- description: Timeout policy
  name: timeoutPolicy
  type: string
- description: Time to wait for worker to respond after polling
  name: responseTimeoutSeconds
  type: integer
- description: Time to wait when polling for task
  name: pollTimeoutSeconds
  type: integer
- description: Concurrent execution limit for the task
  name: concurrentExecLimit
  type: integer
- description: Rate limit per frequency
  name: rateLimitPerFrequency
  type: integer
- description: Rate limit frequency window in seconds
  name: rateLimitFrequencyInSeconds
  type: integer
- description: Email of the task definition owner
  name: ownerEmail
  type: string
- description: Expected input keys
  name: inputKeys
  type: array
- description: Expected output keys
  name: outputKeys
  type: array
- description: Default input template
  name: inputTemplate
  type: object
- description: Creator of the task definition
  name: createdBy
  type: string
- description: Creation timestamp
  name: createTime
  type: integer
- description: Last updater
  name: updatedBy
  type: string
- description: Last update timestamp
  name: updateTime
  type: integer
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/conductor-conductor-task-def-schema.json
slug: conductor-conductor-task-def
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: TaskDef
---
