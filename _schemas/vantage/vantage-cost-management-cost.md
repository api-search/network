---
description: ''
layout: schema
name: Cost
properties_list:
- description: The date of the cost entry.
  name: date
  type: string
- description: The cost amount.
  name: amount
  type: string
- description: The currency of the cost amount.
  name: currency
  type: string
- description: The cloud provider (e.g., aws, azure, gcp).
  name: provider
  type: string
- description: The cloud service name.
  name: service
  type: string
- description: The cloud account identifier.
  name: account_id
  type: string
- description: The cloud region.
  name: region
  type: string
- description: The cost category.
  name: category
  type: string
- description: The cost subcategory.
  name: subcategory
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-cost-schema.json
slug: vantage-cost-management-cost
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Cost
---
