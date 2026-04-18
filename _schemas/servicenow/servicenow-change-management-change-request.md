---
description: A ServiceNow change request record.
layout: schema
name: ChangeRequest
properties_list:
- description: Unique identifier for the change request.
  name: sys_id
  type: string
- description: The human-readable change request number.
  name: number
  type: string
- description: A brief summary of the change.
  name: short_description
  type: string
- description: A detailed description of the change and its purpose.
  name: description
  type: string
- description: 'The change type: normal, standard, or emergency.'
  name: type
  type: string
- description: The current state of the change request in its lifecycle.
  name: state
  type: string
- description: The priority level of the change request.
  name: priority
  type: string
- description: The risk level assessed for this change.
  name: risk
  type: string
- description: The impact level of this change.
  name: impact
  type: string
- description: The category of the change.
  name: category
  type: string
- description: The sys_id of the user assigned to implement the change.
  name: assigned_to
  type: string
- description: The sys_id of the group responsible for the change.
  name: assignment_group
  type: string
- description: The sys_id of the user who requested the change.
  name: requested_by
  type: string
- description: The planned start date and time for the change.
  name: start_date
  type: string
- description: The planned end date and time for the change.
  name: end_date
  type: string
- description: The sys_id of the configuration item affected by this change.
  name: cmdb_ci
  type: string
- description: The close code indicating how the change was resolved.
  name: close_code
  type: string
- description: Notes recorded when closing the change request.
  name: close_notes
  type: string
- description: The current approval status.
  name: approval
  type: string
- description: The date and time the change request was created.
  name: sys_created_on
  type: string
- description: The date and time the change request was last updated.
  name: sys_updated_on
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-change-management-change-request-schema.json
slug: servicenow-change-management-change-request
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
title: ChangeRequest
---
