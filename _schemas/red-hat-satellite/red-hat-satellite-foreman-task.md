---
description: An asynchronous task object returned for long-running operations such as publishing content views or uploading manifests.
layout: schema
name: ForemanTask
properties_list:
- description: Unique task identifier.
  name: id
  type: string
- description: Machine-readable task label.
  name: label
  type: string
- description: Whether the task is still pending.
  name: pending
  type: boolean
- description: Human-readable description of the task action.
  name: action
  type: string
- description: User who initiated the task.
  name: username
  type: string
- description: Current state of the task.
  name: state
  type: string
- description: Result of the task.
  name: result
  type: string
- description: Task progress as a decimal (0.0 to 1.0).
  name: progress
  type: number
- description: ''
  name: started_at
  type: '[''string'', ''null'']'
- description: ''
  name: ended_at
  type: '[''string'', ''null'']'
- description: ''
  name: humanized
  type: object
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-foreman-task-schema.json
slug: red-hat-satellite-foreman-task
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: ForemanTask
---
