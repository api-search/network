---
description: A task associated with a change request.
layout: schema
name: ChangeTask
properties_list:
- description: Unique identifier for the change task.
  name: sys_id
  type: string
- description: The human-readable task number.
  name: number
  type: string
- description: A brief summary of the task.
  name: short_description
  type: string
- description: The current state of the task.
  name: state
  type: string
- description: The sys_id of the assigned user.
  name: assigned_to
  type: string
- description: The sys_id of the parent change request.
  name: change_request
  type: string
- description: The planned start date for the task.
  name: planned_start_date
  type: string
- description: The planned end date for the task.
  name: planned_end_date
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-change-management-change-task-schema.json
slug: servicenow-change-management-change-task
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: ChangeTask
---
