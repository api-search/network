---
description: Fields for creating a change task.
layout: schema
name: ChangeTaskInput
properties_list:
- description: A brief summary of the task.
  name: short_description
  type: string
- description: A detailed description of the task.
  name: description
  type: string
- description: The sys_id of the assigned user.
  name: assigned_to
  type: string
- description: The sys_id of the assignment group.
  name: assignment_group
  type: string
- description: The planned start date.
  name: planned_start_date
  type: string
- description: The planned end date.
  name: planned_end_date
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-change-management-change-task-input-schema.json
slug: servicenow-change-management-change-task-input
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
title: ChangeTaskInput
---
