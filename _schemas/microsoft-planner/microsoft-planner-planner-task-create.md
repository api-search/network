---
description: Request body for creating a new task
layout: schema
name: PlannerTaskCreate
properties_list:
- description: ID of the plan the task belongs to
  name: planId
  type: string
- description: Title of the task
  name: title
  type: string
- description: ID of the bucket to place the task in
  name: bucketId
  type: string
- description: Priority of the task (0 is highest, 10 is lowest)
  name: priority
  type: integer
- description: ''
  name: percentComplete
  type: integer
- description: ''
  name: startDateTime
  type: string
- description: ''
  name: dueDateTime
  type: string
- description: ''
  name: conversationThreadId
  type: string
- description: ''
  name: orderHint
  type: string
- description: ''
  name: assigneePriority
  type: string
provider_name: Microsoft Planner
provider_slug: microsoft-planner
schema_file: json-schema/microsoft-planner-planner-task-create-schema.json
slug: microsoft-planner-planner-task-create
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
title: PlannerTaskCreate
---
