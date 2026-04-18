---
description: An Access Grant that assigns a specific level of access to a Vantage resource for a Team.
layout: schema
name: Vantage Access Grant
properties_list:
- description: The unique token identifier for the Access Grant.
  name: token
  type: string
- description: The token of the Team the grant applies to.
  name: team_token
  type: string
- description: The token of the resource being granted access to.
  name: resource_token
  type: string
- description: The level of access granted.
  name: access
  type: string
- description: The date and time the Access Grant was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/access-grant.json
slug: access-grant
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Access Grant
---
