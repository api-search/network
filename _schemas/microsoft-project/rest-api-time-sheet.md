---
description: TimeSheet schema from Microsoft Project Online REST API
layout: schema
name: TimeSheet
properties_list:
- description: Timesheet identifier
  name: Id
  type: string
- description: Timesheet status (0=InProgress, 1=Submitted, 2=Acceptable, 3=Approved, 4=Rejected)
  name: Status
  type: integer
- description: Associated period ID
  name: PeriodId
  type: string
- description: Total work reported
  name: TotalWork
  type: string
- description: Total actual work
  name: TotalActualWork
  type: string
provider_name: Microsoft Project
provider_slug: microsoft-project
schema_file: json-schema/rest-api-time-sheet-schema.json
slug: rest-api-time-sheet
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
title: TimeSheet
---
