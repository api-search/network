---
description: An employee leave allowance record for a specific reason type and year.
layout: schema
name: Allowance
properties_list:
- description: Unique identifier of the allowance.
  name: _id
  type: string
- description: ID of the user this allowance belongs to.
  name: userId
  type: string
- description: ID of the absence reason type this allowance is for.
  name: reasonId
  type: string
- description: Calendar year this allowance applies to.
  name: year
  type: integer
- description: Total number of days allowed.
  name: allowance
  type: number
- description: Number of days used.
  name: used
  type: number
- description: Number of days remaining.
  name: remaining
  type: number
- description: Number of days carried over from the previous year.
  name: carryover
  type: number
provider_name: Absence.io
provider_slug: absence-io
schema_file: json-schema/allowance-schema.json
slug: allowance
tags:
- Absences
- Employees
- Leave Management
- HR
title: Allowance
---
