---
description: ''
layout: schema
name: Dashboard
properties_list:
- description: The unique token identifier for the Dashboard.
  name: token
  type: string
- description: The title of the Dashboard.
  name: title
  type: string
- description: Tokens of widgets included in the Dashboard.
  name: widget_tokens
  type: array
- description: The token of the Workspace this Dashboard belongs to.
  name: workspace_token
  type: string
- description: The date and time the Dashboard was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-dashboard-schema.json
slug: vantage-cost-management-dashboard
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Dashboard
---
