---
description: Assignment schema from Microsoft Project Online REST API
layout: schema
name: Assignment
properties_list:
- description: Assignment identifier
  name: Id
  type: string
- description: Project identifier
  name: ProjectId
  type: string
- description: Task identifier
  name: TaskId
  type: string
- description: Resource identifier
  name: ResourceId
  type: string
- description: Name of the assigned resource
  name: ResourceName
  type: string
- description: Actual work completed
  name: ActualWork
  type: string
- description: Remaining work
  name: RemainingWork
  type: string
- description: Work completion percentage
  name: PercentWorkComplete
  type: integer
- description: Assignment start date
  name: Start
  type: string
- description: Assignment finish date
  name: Finish
  type: string
provider_name: Microsoft Project
provider_slug: microsoft-project
schema_file: json-schema/rest-api-assignment-schema.json
slug: rest-api-assignment
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
title: Assignment
---
