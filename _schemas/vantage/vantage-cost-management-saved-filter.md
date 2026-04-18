---
description: ''
layout: schema
name: SavedFilter
properties_list:
- description: The unique token identifier for the Saved Filter.
  name: token
  type: string
- description: The title of the Saved Filter.
  name: title
  type: string
- description: The VQL filter expression.
  name: filter
  type: string
- description: The token of the Workspace this Saved Filter belongs to.
  name: workspace_token
  type: string
- description: The date and time the Saved Filter was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-saved-filter-schema.json
slug: vantage-cost-management-saved-filter
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: SavedFilter
---
