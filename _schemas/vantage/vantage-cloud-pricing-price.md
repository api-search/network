---
description: ''
layout: schema
name: Price
properties_list:
- description: The unique identifier for the Price.
  name: id
  type: string
- description: The pricing unit (e.g., per hour, per GB-month).
  name: unit
  type: string
- description: The price amount.
  name: price
  type: string
- description: The currency of the price.
  name: currency
  type: string
- description: The cloud region this price applies to.
  name: region
  type: string
- description: A description of the pricing tier or option.
  name: description
  type: string
- description: The identifier of the associated Product.
  name: product_id
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cloud-pricing-price-schema.json
slug: vantage-cloud-pricing-price
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Price
---
