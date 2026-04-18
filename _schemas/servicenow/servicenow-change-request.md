---
description: A ServiceNow change request record used for managing planned changes to IT services and infrastructure within the ITSM Change Management process.
layout: schema
name: ServiceNow Change Request
properties_list:
- description: The unique 32-character system identifier for the change request.
  name: sys_id
  type: string
- description: The human-readable change request number, prefixed with CHG.
  name: number
  type: string
- description: A brief summary of the change.
  name: short_description
  type: string
- description: A detailed description of the change and its purpose.
  name: description
  type:
  - string
  - 'null'
- description: 'The change type: normal requires approval, standard uses pre-approved templates, emergency bypasses normal approval.'
  name: type
  type: string
- description: 'The change lifecycle state: -5=New, -4=Assess, -3=Authorize, -2=Scheduled, -1=Implement, 0=Review, 3=Closed, 4=Canceled.'
  name: state
  type: string
- description: The current phase of the change request.
  name: phase
  type:
  - string
  - 'null'
- description: 'The priority level: 1=Critical, 2=High, 3=Moderate, 4=Low.'
  name: priority
  type: string
- description: The assessed risk level of the change.
  name: risk
  type:
  - string
  - 'null'
- description: 'The impact level: 1=High, 2=Medium, 3=Low.'
  name: impact
  type: string
- description: The category of the change.
  name: category
  type:
  - string
  - 'null'
- description: The user assigned to implement the change.
  name: assigned_to
  type: object
- description: The group responsible for the change.
  name: assignment_group
  type: object
- description: The user who requested the change.
  name: requested_by
  type: object
- description: The user who created the change request.
  name: opened_by
  type: object
- description: The planned start date and time for implementing the change.
  name: start_date
  type:
  - string
  - 'null'
- description: The planned end date and time for the change implementation.
  name: end_date
  type:
  - string
  - 'null'
- description: The configuration item affected by the change.
  name: cmdb_ci
  type: object
- description: The business service impacted by the change.
  name: business_service
  type: object
- description: The business justification for the change.
  name: justification
  type:
  - string
  - 'null'
- description: The plan for implementing the change.
  name: implementation_plan
  type:
  - string
  - 'null'
- description: The plan for reverting the change if problems occur.
  name: backout_plan
  type:
  - string
  - 'null'
- description: The plan for testing the change.
  name: test_plan
  type:
  - string
  - 'null'
- description: Analysis of the potential risks and impact of the change.
  name: risk_impact_analysis
  type:
  - string
  - 'null'
- description: The current approval status of the change.
  name: approval
  type:
  - string
  - 'null'
- description: Whether the change requires a Change Advisory Board review.
  name: cab_required
  type: boolean
- description: The code indicating how the change was resolved.
  name: close_code
  type:
  - string
  - 'null'
- description: Notes recorded when closing the change request.
  name: close_notes
  type:
  - string
  - 'null'
- description: The conflict checking status.
  name: conflict_status
  type:
  - string
  - 'null'
- description: Whether the change is currently on hold.
  name: on_hold
  type: boolean
- description: The reason the change is on hold.
  name: on_hold_reason
  type:
  - string
  - 'null'
- description: Whether the change request is active.
  name: active
  type: boolean
- description: The date and time the change was opened.
  name: opened_at
  type: string
- description: The date and time the change was closed.
  name: closed_at
  type:
  - string
  - 'null'
- description: The date and time the record was created.
  name: sys_created_on
  type: string
- description: The user who created the record.
  name: sys_created_by
  type: string
- description: The date and time the record was last updated.
  name: sys_updated_on
  type: string
- description: The user who last updated the record.
  name: sys_updated_by
  type: string
- description: The number of times the record has been modified.
  name: sys_mod_count
  type: integer
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-change-request-schema.json
slug: servicenow-change-request
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
title: ServiceNow Change Request
---
