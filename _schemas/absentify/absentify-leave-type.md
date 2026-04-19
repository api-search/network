---
description: A leave type defined in the absentify workspace.
layout: schema
name: LeaveType
properties_list:
- description: Unique identifier of the leave type.
  name: id
  type: string
- description: Name of the leave type.
  name: name
  type: string
- description: Unit for this leave type (days or hours).
  name: leave_unit
  type: string
- description: Color code for this leave type.
  name: color
  type: string
- description: Icon for this leave type.
  name: icon
  type: string
- description: Timestamp when the leave type was created.
  name: createdAt
  type: string
- description: Timestamp when the leave type was last updated.
  name: updatedAt
  type: string
provider_name: Absentify
provider_slug: absentify
schema_file: json-schema/absentify-leave-type-schema.json
slug: absentify-leave-type
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
title: LeaveType
---
