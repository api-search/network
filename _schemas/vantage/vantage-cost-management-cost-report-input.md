---
description: ''
layout: schema
name: CostReportInput
properties_list:
- description: The title of the Cost Report.
  name: title
  type: string
- description: VQL filter expression for the Cost Report.
  name: filter
  type: string
- description: Groupings for the Cost Report.
  name: groupings
  type: string
- description: The token of the Folder to place the report in.
  name: folder_token
  type: string
- description: Tokens of Saved Filters to apply.
  name: saved_filter_tokens
  type: array
- description: The token of the Workspace for the report.
  name: workspace_token
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-cost-report-input-schema.json
slug: vantage-cost-management-cost-report-input
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: CostReportInput
---
