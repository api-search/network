---
description: A Team that groups users together for managing access to Vantage resources within a Workspace.
layout: schema
name: Vantage Team
properties_list:
- description: The unique token identifier for the Team.
  name: token
  type: string
- description: The name of the Team.
  name: name
  type: string
- description: The description of the Team.
  name: description
  type: string
- description: The token of the Workspace this Team belongs to.
  name: workspace_token
  type: string
- description: Tokens of users who are members of the Team.
  name: user_tokens
  type: array
- description: The date and time the Team was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/team.json
slug: team
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Team
---
