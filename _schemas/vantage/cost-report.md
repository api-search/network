---
description: A Cost Report in Vantage that tracks and visualizes cloud spending using VQL filters and groupings across providers.
layout: schema
name: Vantage Cost Report
properties_list:
- description: The unique token identifier for the Cost Report.
  name: token
  type: string
- description: The title of the Cost Report.
  name: title
  type: string
- description: The VQL filter applied to the Cost Report.
  name: filter
  type: string
- description: The groupings applied to the Cost Report.
  name: groupings
  type: string
- description: The token of the Folder this report belongs to.
  name: folder_token
  type: string
- description: Tokens of Saved Filters applied to this report.
  name: saved_filter_tokens
  type: array
- description: The token of the Workspace this report belongs to.
  name: workspace_token
  type: string
- description: The date and time the Cost Report was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/cost-report.json
slug: cost-report
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Cost Report
---
