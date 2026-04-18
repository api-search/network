---
description: An Integration connecting a cloud provider account to Vantage for cost data collection.
layout: schema
name: Vantage Integration
properties_list:
- description: The unique token identifier for the Integration.
  name: token
  type: string
- description: The cloud provider (e.g., aws, azure, gcp).
  name: provider
  type: string
- description: The current status of the Integration.
  name: status
  type: string
- description: The cloud account identifier for the Integration.
  name: account_identifier
  type: string
- description: The date and time the Integration was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/integration.json
slug: integration
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: Vantage Integration
---
