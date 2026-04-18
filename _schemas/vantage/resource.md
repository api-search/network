---
description: A cloud Resource with associated cost, provider, service, and regional metadata.
layout: schema
name: Vantage Resource
properties_list:
- description: The unique identifier for the Resource.
  name: token
  type: string
- description: The name of the Resource.
  name: name
  type: string
- description: The cloud provider.
  name: provider
  type: string
- description: The cloud service.
  name: service
  type: string
- description: The cloud account identifier.
  name: account_id
  type: string
- description: The region of the resource.
  name: region
  type: string
- description: The cost associated with the resource.
  name: cost
  type: string
- description: Additional metadata about the resource.
  name: metadata
  type: object
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/resource.json
slug: resource
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Resource
---
