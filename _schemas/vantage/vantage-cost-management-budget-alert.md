---
description: ''
layout: schema
name: BudgetAlert
properties_list:
- description: The unique token identifier for the Budget Alert.
  name: token
  type: string
- description: The token of the associated Cost Report.
  name: cost_report_token
  type: string
- description: The budget amount.
  name: budget
  type: string
- description: The budget period (e.g., monthly).
  name: period
  type: string
- description: The date and time the Budget Alert was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-budget-alert-schema.json
slug: vantage-cost-management-budget-alert
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: BudgetAlert
---
