---
description: An absence reason type (e.g., vacation, sick leave, parental leave).
layout: schema
name: ReasonType
properties_list:
- description: Unique identifier of the reason type.
  name: _id
  type: string
- description: Display name of the absence reason.
  name: name
  type: string
- description: Color code for displaying this absence type in the calendar.
  name: color
  type: string
- description: Whether absences of this type require manager approval.
  name: requiresApproval
  type: boolean
- description: Whether absences of this type count against the employee's allowance.
  name: affectsAllowance
  type: boolean
provider_name: Absence.io
provider_slug: absence-io
schema_file: json-schema/reason-type-schema.json
slug: reason-type
tags:
- Absences
- Employees
- Leave Management
- HR
title: ReasonType
---
