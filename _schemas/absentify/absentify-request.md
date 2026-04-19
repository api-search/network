---
description: A leave request in absentify.
layout: schema
name: Request
properties_list:
- description: Unique identifier of the request.
  name: id
  type: string
- description: Start date of the request.
  name: start
  type: string
- description: Time of day when the leave starts.
  name: start_at
  type: string
- description: End date of the request.
  name: end
  type: string
- description: Time of day when the leave ends.
  name: end_at
  type: string
- description: Current status of the request.
  name: status
  type: string
- description: Reason for the leave request.
  name: reason
  type: string
- description: Duration of the leave.
  name: duration
  type: number
- description: Timestamp when the request was created.
  name: createdAt
  type: string
- description: Timestamp when the request was last updated.
  name: updatedAt
  type: string
provider_name: Absentify
provider_slug: absentify
schema_file: json-schema/absentify-request-schema.json
slug: absentify-request
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
title: Request
---
