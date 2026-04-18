---
description: A cloud Service within a Provider, containing products with pricing data.
layout: schema
name: Vantage Cloud Pricing Service
properties_list:
- description: The unique identifier for the Service.
  name: id
  type: string
- description: The display name of the Service.
  name: name
  type: string
- description: The identifier of the Provider this Service belongs to.
  name: provider_id
  type: string
- description: The number of products available in this Service.
  name: products_count
  type: integer
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/service.json
slug: service
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Cloud Pricing Service
---
