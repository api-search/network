---
description: A Budget Alert that monitors cloud spending against a defined budget threshold for a Cost Report.
layout: schema
name: Vantage Budget Alert
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
schema_file: json-schema/budget-alert.json
slug: budget-alert
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Budget Alert
---
