---
description: A top-level Acronis backup or protection task
layout: schema
name: Task
properties_list:
- description: Task unique identifier
  name: id
  type: string
- description: Task UUID
  name: uuid
  type: string
- description: Task type (backup, restore, replication, etc.)
  name: type
  type: string
- description: Current task state
  name: state
  type: string
- description: Task result upon completion
  name: result_code
  type: string
- description: Task execution priority
  name: priority
  type: string
- description: Protection policy that initiated this task
  name: policy_id
  type: string
- description: Protected resource this task operates on
  name: resource_id
  type: string
- description: Agent or executor that ran the task
  name: executor_id
  type: string
- description: When the task was queued
  name: enqueuedAt
  type: string
- description: When task execution began
  name: startedAt
  type: string
- description: When task completed
  name: completedAt
  type: string
- description: ''
  name: updatedAt
  type: string
- description: ''
  name: tenant_id
  type: string
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/task-manager-task-schema.json
slug: task-manager-task
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: Task
---
