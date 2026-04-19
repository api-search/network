---
description: A prepaid credit order for a customer
layout: schema
name: PrepaidOrder
properties_list:
- description: Unique prepaid order identifier
  name: orderId
  type: string
- description: Customer identifier
  name: customerId
  type: string
- description: Prepaid credit amount
  name: amount
  type: number
- description: Currency code
  name: currency
  type: string
- description: Creation timestamp
  name: createTime
  type: integer
- description: Expiration timestamp in Unix milliseconds
  name: expirationTime
  type: integer
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/billing-prepaid-order-schema.json
slug: billing-prepaid-order
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: PrepaidOrder
---
