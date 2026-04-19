---
description: Request body for creating a prepaid order
layout: schema
name: PrepaidOrderRequest
properties_list:
- description: Customer identifier
  name: customerId
  type: string
- description: Prepaid credit amount
  name: amount
  type: number
- description: Currency code
  name: currency
  type: string
- description: Expiration timestamp in Unix milliseconds
  name: expirationTime
  type: integer
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/billing-prepaid-order-request-schema.json
slug: billing-prepaid-order-request
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: PrepaidOrderRequest
---
