---
description: ''
layout: schema
name: AccountResult
properties_list:
- description: Account holder first name.
  name: first_name
  type: string
- description: Account holder last name.
  name: last_name
  type: string
- description: Account email address.
  name: email
  type: string
- description: Name of the current subscription plan.
  name: plan_name
  type: string
- description: Level of the current subscription plan.
  name: plan_level
  type: integer
- description: Date when usage counters reset.
  name: reset_date
  type: string
- description: Team identifier.
  name: team_id
  type: integer
- description: Usage breakdown by request type.
  name: requests
  type: object
- description: Deprecated. Total usage counters.
  name: calls
  type: object
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-account-result-schema.json
slug: hunter-account-result
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: AccountResult
---
