---
description: An AWS Budget that tracks cost, usage, RI utilization, or Savings Plans coverage
layout: schema
name: AWS Budget
properties_list:
- description: The name of the budget. Must be unique within an account.
  name: BudgetName
  type: string
- description: The total amount of cost, usage, RI utilization, or Savings Plans coverage that you want to track
  name: BudgetLimit
  type: object
- description: Filters to apply to the budget (e.g., by service, region, tag)
  name: CostFilters
  type: object
- description: Cost types to include in the budget calculation
  name: CostTypes
  type: object
- description: The period covered by a budget
  name: TimeUnit
  type: string
- description: ''
  name: TimePeriod
  type: object
- description: The type of budget
  name: BudgetType
  type: string
- description: ''
  name: CalculatedSpend
  type: object
provider_name: Amazon Billing And Cost Management
provider_slug: amazon-billing-and-cost-management
schema_file: json-schema/cost-budget-schema.json
slug: cost-budget
tags:
- Billing
- Cost Management
- Cost Explorer
- Budgets
- Cost Optimization
- FinOps
- Amazon Web Services
- AWS
title: AWS Budget
---
