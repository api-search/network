---
description: ''
layout: schema
name: Recommendation
properties_list:
- description: The unique token identifier for the Recommendation.
  name: token
  type: string
- description: The type of recommendation.
  name: type
  type: string
- description: A description of the recommendation.
  name: description
  type: string
- description: The estimated monthly savings.
  name: estimated_savings
  type: string
- description: The cloud provider.
  name: provider
  type: string
- description: The cloud service.
  name: service
  type: string
- description: The resource identifier.
  name: resource_id
  type: string
- description: The date and time the Recommendation was generated.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-recommendation-schema.json
slug: vantage-cost-management-recommendation
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Recommendation
---
