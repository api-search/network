---
description: Task schema from Oracle Integration Process Automation API.
layout: schema
name: Task
properties_list:
- description: Task identifier.
  name: id
  type: string
- description: Task title.
  name: title
  type: string
- description: Current assignee.
  name: assignee
  type: string
- description: Task state.
  name: state
  type: string
- description: Task priority.
  name: priority
  type: integer
- description: Task creation timestamp.
  name: createdDate
  type: string
- description: Task due date.
  name: dueDate
  type: string
- description: Parent process instance identifier.
  name: processId
  type: string
- description: Parent process name.
  name: processName
  type: string
- description: Task outcome.
  name: outcome
  type: string
provider_name: Oracle Integration
provider_slug: oracle-integration
schema_file: json-schema/process-automation-api-task-schema.json
slug: process-automation-api-task
tags:
- API Management
- Automation
- B2B Integration
- Cloud Integration
- Enterprise Integration
- Integration
- iPaaS
- Process Automation
title: Task
---
