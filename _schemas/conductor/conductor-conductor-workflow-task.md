---
description: ''
layout: schema
name: WorkflowTask
properties_list:
- description: Name of the task
  name: name
  type: string
- description: Unique reference name for the task within the workflow
  name: taskReferenceName
  type: string
- description: The type of task
  name: type
  type: string
- description: Task description
  name: description
  type: string
- description: Input parameter mappings
  name: inputParameters
  type: object
- description: Whether this task is optional
  name: optional
  type: boolean
- description: Delay in seconds before starting the task
  name: startDelay
  type: integer
- description: Whether the task is completed asynchronously
  name: asyncComplete
  type: boolean
- description: Number of retries
  name: retryCount
  type: integer
- description: Sink for EVENT tasks
  name: sink
  type: string
- description: Sub workflow parameters
  name: subWorkflowParam
  type: object
- description: List of task reference names to join on
  name: joinOn
  type: array
- description: List of forked task lists
  name: forkTasks
  type: array
- description: Decision cases for SWITCH/DECISION tasks
  name: decisionCases
  type: object
- description: Default case tasks for SWITCH/DECISION
  name: defaultCase
  type: array
- description: Loop condition for DO_WHILE tasks
  name: loopCondition
  type: string
- description: Tasks to loop over in DO_WHILE
  name: loopOver
  type: array
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/conductor-conductor-workflow-task-schema.json
slug: conductor-conductor-workflow-task
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: WorkflowTask
---
