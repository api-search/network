---
description: ''
layout: schema
name: Workflow
properties_list:
- description: Unique workflow instance ID
  name: workflowId
  type: string
- description: Name of the workflow definition
  name: workflowName
  type: string
- description: Version of the workflow definition
  name: workflowVersion
  type: integer
- description: Correlation ID
  name: correlationId
  type: string
- description: Current status of the workflow
  name: status
  type: string
- description: Start time in epoch milliseconds
  name: startTime
  type: integer
- description: End time in epoch milliseconds
  name: endTime
  type: integer
- description: Last update time
  name: updateTime
  type: integer
- description: Workflow input
  name: input
  type: object
- description: Workflow output
  name: output
  type: object
- description: List of tasks in the workflow execution
  name: tasks
  type: array
- description: Reason for failure or termination
  name: reasonForIncompletion
  type: string
- description: List of failed task reference names
  name: failedReferenceTaskNames
  type: array
- description: Workflow priority
  name: priority
  type: integer
- description: Workflow variables
  name: variables
  type: object
- description: Last retry timestamp
  name: lastRetriedTime
  type: integer
- description: Owner application
  name: ownerApp
  type: string
- description: Creation timestamp
  name: createTime
  type: integer
- description: Created by
  name: createdBy
  type: string
- description: Parent workflow ID if this is a sub-workflow
  name: parentWorkflowId
  type: string
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/conductor-conductor-workflow-schema.json
slug: conductor-conductor-workflow
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: Workflow
---
