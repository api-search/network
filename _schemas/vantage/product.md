---
description: A cloud infrastructure Product with pricing details, such as an EC2 instance type or storage tier.
layout: schema
name: Vantage Cloud Pricing Product
properties_list:
- description: The unique identifier for the Product.
  name: id
  type: string
- description: The display name of the Product.
  name: name
  type: string
- description: The identifier of the cloud Provider.
  name: provider_id
  type: string
- description: The identifier of the Service.
  name: service_id
  type: string
- description: Product-specific details such as vCPUs, memory, storage, network performance, etc.
  name: details
  type: object
- description: Pricing data for this Product across regions.
  name: prices
  type: array
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/product.json
slug: product
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Cloud Pricing Product
---
