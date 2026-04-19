---
description: ''
layout: schema
name: TaskResult
properties_list:
- description: The workflow instance ID
  name: workflowInstanceId
  type: string
- description: The task ID
  name: taskId
  type: string
- description: Task execution status
  name: status
  type: string
- description: Task output data
  name: outputData
  type: object
- description: Reason for failure
  name: reasonForIncompletion
  type: string
- description: Callback delay for IN_PROGRESS tasks
  name: callbackAfterSeconds
  type: integer
- description: ID of the worker updating the task
  name: workerId
  type: string
- description: Task execution logs
  name: logs
  type: array
- description: Path to externally stored output payload
  name: externalOutputPayloadStoragePath
  type: string
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/conductor-conductor-task-result-schema.json
slug: conductor-conductor-task-result
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: TaskResult
---
