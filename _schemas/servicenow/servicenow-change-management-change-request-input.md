---
description: Fields for creating or updating a change request.
layout: schema
name: ChangeRequestInput
properties_list:
- description: A brief summary of the change.
  name: short_description
  type: string
- description: A detailed description of the change.
  name: description
  type: string
- description: The priority level.
  name: priority
  type: string
- description: The risk level.
  name: risk
  type: string
- description: The impact level.
  name: impact
  type: string
- description: The category of the change.
  name: category
  type: string
- description: The sys_id of the assigned user.
  name: assigned_to
  type: string
- description: The sys_id of the assignment group.
  name: assignment_group
  type: string
- description: The sys_id of the requesting user.
  name: requested_by
  type: string
- description: The planned start date and time.
  name: start_date
  type: string
- description: The planned end date and time.
  name: end_date
  type: string
- description: The sys_id of the affected configuration item.
  name: cmdb_ci
  type: string
- description: The business justification for the change.
  name: justification
  type: string
- description: The plan for implementing the change.
  name: implementation_plan
  type: string
- description: The plan for reverting the change if needed.
  name: backout_plan
  type: string
- description: The plan for testing the change.
  name: test_plan
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-change-management-change-request-input-schema.json
slug: servicenow-change-management-change-request-input
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
title: ChangeRequestInput
---
