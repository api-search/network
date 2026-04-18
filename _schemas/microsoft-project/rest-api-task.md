---
description: Task schema from Microsoft Project Online REST API
layout: schema
name: Task
properties_list:
- description: Unique identifier of the task
  name: Id
  type: string
- description: Name of the task
  name: Name
  type: string
- description: Task start date
  name: Start
  type: string
- description: Task finish date
  name: Finish
  type: string
- description: Task duration in days
  name: Duration
  type: string
- description: Task completion percentage
  name: PercentComplete
  type: integer
- description: Whether this is a summary task
  name: IsSummary
  type: boolean
- description: Whether this is a milestone
  name: IsMilestone
  type: boolean
- description: Task priority (0-1000)
  name: Priority
  type: integer
- description: Parent task ID for subtasks
  name: ParentId
  type: string
- description: Task notes
  name: Notes
  type: string
- description: Whether the task is manually scheduled
  name: IsManuallyScheduled
  type: boolean
- description: Scheduling constraint type
  name: ConstraintType
  type: integer
- description: Constraint date
  name: ConstraintStartEnd
  type: string
- description: Total scheduled work
  name: Work
  type: string
- description: Remaining work
  name: RemainingWork
  type: string
- description: Actual work completed
  name: ActualWork
  type: string
- description: Total cost
  name: Cost
  type: number
provider_name: Microsoft Project
provider_slug: microsoft-project
schema_file: json-schema/rest-api-task-schema.json
slug: rest-api-task
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
title: Task
---
