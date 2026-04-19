---
description: A member (employee) in the absentify workspace.
layout: schema
name: Member
properties_list:
- description: Unique identifier of the member.
  name: id
  type: string
- description: Custom identifier for the member.
  name: custom_id
  type: string
- description: Name of the member.
  name: name
  type: string
- description: Email address of the member.
  name: email
  type: string
- description: Current status of the member.
  name: status
  type: string
- description: Whether the member is an admin.
  name: is_admin
  type: boolean
- description: Approval process type for this member.
  name: approval_process
  type: string
- description: Employment start date.
  name: employment_start_date
  type: string
- description: Employment end date if applicable.
  name: employment_end_date
  type: string
- description: Birthday of the member.
  name: birthday
  type: string
- description: Timestamp when the member was created.
  name: createdAt
  type: string
- description: Timestamp when the member was last updated.
  name: updatedAt
  type: string
provider_name: Absentify
provider_slug: absentify
schema_file: json-schema/absentify-member-schema.json
slug: absentify-member
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
title: Member
---
