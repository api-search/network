---
description: A Conductor event handler definition that specifies how to respond to events by triggering workflows, completing tasks, or failing tasks based on configurable conditions.
layout: schema
name: EventHandler
properties_list:
- description: Name of the event handler
  name: name
  type: string
- description: Event identifier in the format source:sink:subject (e.g., conductor:workflow_completed:myWorkflow)
  name: event
  type: string
- description: Condition expression to evaluate
  name: condition
  type: string
- description: List of actions to perform when the event is received
  name: actions
  type: array
- description: Whether the event handler is active
  name: active
  type: boolean
- description: Type of evaluator for the condition
  name: evaluatorType
  type: string
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/event-handler.json
slug: event-handler
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: EventHandler
---
