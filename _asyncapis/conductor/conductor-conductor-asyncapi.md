---
channels:
- description: Emitted when a workflow execution is started
  name: workflow.started
  operation: subscribe
  operation_id: onWorkflowStarted
  summary: Receive workflow started events
- description: Emitted when a workflow execution completes successfully
  name: workflow.completed
  operation: subscribe
  operation_id: onWorkflowCompleted
  summary: Receive workflow completed events
- description: Emitted when a workflow execution fails
  name: workflow.failed
  operation: subscribe
  operation_id: onWorkflowFailed
  summary: Receive workflow failed events
- description: Emitted when a workflow execution is terminated
  name: workflow.terminated
  operation: subscribe
  operation_id: onWorkflowTerminated
  summary: Receive workflow terminated events
- description: Emitted when a workflow execution times out
  name: workflow.timed_out
  operation: subscribe
  operation_id: onWorkflowTimedOut
  summary: Receive workflow timed out events
- description: Emitted when a workflow execution is paused
  name: workflow.paused
  operation: subscribe
  operation_id: onWorkflowPaused
  summary: Receive workflow paused events
- description: Emitted when a task is scheduled for execution
  name: task.scheduled
  operation: subscribe
  operation_id: onTaskScheduled
  summary: Receive task scheduled events
- description: Emitted when a task execution begins
  name: task.in_progress
  operation: subscribe
  operation_id: onTaskInProgress
  summary: Receive task in progress events
- description: Emitted when a task execution completes successfully
  name: task.completed
  operation: subscribe
  operation_id: onTaskCompleted
  summary: Receive task completed events
- description: Emitted when a task execution fails
  name: task.failed
  operation: subscribe
  operation_id: onTaskFailed
  summary: Receive task failed events
- description: Emitted when a task execution times out
  name: task.timed_out
  operation: subscribe
  operation_id: onTaskTimedOut
  summary: Receive task timed out events
- description: Emitted when a task execution is canceled
  name: task.canceled
  operation: subscribe
  operation_id: onTaskCanceled
  summary: Receive task canceled events
description: Asynchronous event API for Conductor workflow orchestration platform. Conductor emits events when workflows and tasks change state, enabling reactive event-driven architectures. Event handlers can be configured to trigger workflows, complete tasks, or fail tasks in response to these events.
layout: asyncapi
messages:
- description: ''
  name: WorkflowStatusEvent
  summary: An event indicating a change in workflow execution status
  title: Workflow Status Event
- description: ''
  name: TaskStatusEvent
  summary: An event indicating a change in task execution status
  title: Task Status Event
name: Conductor Events API
provider_name: Conductor
provider_slug: conductor
servers:
- description: Local Conductor Server
  name: local
  protocol: http
  url: localhost:8080
- description: Orkes Conductor Playground
  name: playground
  protocol: https
  url: play.orkes.io
slug: conductor-conductor-asyncapi
spec_file: asyncapi/conductor-conductor-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/conductor/refs/heads/main/asyncapi/conductor-conductor-asyncapi.yml
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
- AsyncAPI
- Webhooks
- Events
version: 3.x
---
