---
description: ''
layout: schema
name: ManagedAccount
properties_list:
- description: The unique token identifier for the Managed Account.
  name: token
  type: string
- description: The name of the Managed Account.
  name: name
  type: string
- description: The cloud provider account identifier.
  name: account_identifier
  type: string
- description: The cloud provider.
  name: provider
  type: string
- description: The date and time the Managed Account was created.
  name: created_at
  type: string
provider_name: Vantage
provider_slug: vantage
schema_file: json-schema/vantage-cost-management-managed-account-schema.json
slug: vantage-cost-management-managed-account
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
title: ManagedAccount
---
