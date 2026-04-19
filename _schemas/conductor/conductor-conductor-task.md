---
description: ''
layout: schema
name: Task
properties_list:
- description: Unique task instance ID
  name: taskId
  type: string
- description: The type of the task
  name: taskType
  type: string
- description: Current status of the task
  name: status
  type: string
- description: Reference name of the task in the workflow
  name: referenceTaskName
  type: string
- description: ID of the workflow instance this task belongs to
  name: workflowInstanceId
  type: string
- description: Type/name of the workflow
  name: workflowType
  type: string
- description: Correlation ID
  name: correlationId
  type: string
- description: Scheduled time
  name: scheduledTime
  type: integer
- description: Start time
  name: startTime
  type: integer
- description: End time
  name: endTime
  type: integer
- description: Last update time
  name: updateTime
  type: integer
- description: Current retry count
  name: retryCount
  type: integer
- description: Number of times this task was polled
  name: pollCount
  type: integer
- description: Callback delay in seconds
  name: callbackAfterSeconds
  type: integer
- description: ID of the worker that polled this task
  name: workerId
  type: string
- description: Task input data
  name: inputData
  type: object
- description: Task output data
  name: outputData
  type: object
- description: Reason for failure
  name: reasonForIncompletion
  type: string
- description: Task execution logs
  name: logs
  type: array
- description: Task domain
  name: domain
  type: string
- description: Sequence number
  name: seq
  type: integer
- description: Task definition name
  name: taskDefName
  type: string
- description: Response timeout
  name: responseTimeoutSeconds
  type: integer
- description: Time spent waiting in queue
  name: queueWaitTime
  type: integer
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/conductor-conductor-task-schema.json
slug: conductor-conductor-task
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: Task
---
