---
description: An absence entry for a specific date and member.
layout: schema
name: Absence
properties_list:
- description: Unique identifier of the absence.
  name: id
  type: string
- description: Date of the absence.
  name: date
  type: string
- description: Duration of the absence (0.5 for half day, 1 for full day).
  name: duration
  type: number
- description: ID of the associated leave request.
  name: request_id
  type: string
provider_name: Absentify
provider_slug: absentify
schema_file: json-schema/absentify-absence-schema.json
slug: absentify-absence
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
title: Absence
---
