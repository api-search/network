---
description: An employee absence record.
layout: schema
name: Absence
properties_list:
- description: Unique identifier of the absence.
  name: _id
  type: string
- description: ID of the user this absence is assigned to.
  name: assignedToId
  type: string
- description: ID of the absence reason type.
  name: reasonId
  type: string
- description: ID of the user who approved this absence.
  name: approverId
  type: string
- description: Start date and time of the absence.
  name: start
  type: string
- description: End date and time of the absence.
  name: end
  type: string
- description: Number of working days covered by the absence.
  name: days
  type: number
- description: 'Absence approval status: 0=pending, 1=approved, 2=declined.'
  name: status
  type: integer
- description: Optional comment or note on the absence.
  name: comment
  type: string
provider_name: Absence.io
provider_slug: absence-io
schema_file: json-schema/absence-schema.json
slug: absence
tags:
- Absences
- Employees
- Leave Management
- HR
title: Absence
---
