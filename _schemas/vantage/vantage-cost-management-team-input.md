---
description: ''
layout: schema
name: TeamInput
properties_list:
- description: The name of the Team.
  name: name
  type: string
- description: The description of the Team.
  name: description
  type: string
- description: The token of the Workspace for the Team.
  name: workspace_token
  type: string
- description: Tokens of users to add to the Team.
  name: user_tokens
  type: array
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-team-input-schema.json
slug: vantage-cost-management-team-input
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: TeamInput
---
