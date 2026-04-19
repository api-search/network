---
description: ''
layout: schema
name: EventHandlerAction
properties_list:
- description: The action type
  name: action
  type: string
- description: Start workflow action parameters
  name: start_workflow
  type: object
- description: Complete task action parameters
  name: complete_task
  type: object
- description: Fail task action parameters
  name: fail_task
  type: object
- description: Whether to expand inline JSON strings
  name: expandInlineJSON
  type: boolean
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/conductor-conductor-event-handler-action-schema.json
slug: conductor-conductor-event-handler-action
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: EventHandlerAction
---
