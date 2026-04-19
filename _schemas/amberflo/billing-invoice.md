---
description: A customer invoice
layout: schema
name: Invoice
properties_list:
- description: Unique invoice identifier
  name: invoiceId
  type: string
- description: Customer identifier
  name: customerId
  type: string
- description: Invoice period start in Unix seconds
  name: startTime
  type: integer
- description: Invoice period end in Unix seconds
  name: endTime
  type: integer
- description: Total invoice amount
  name: totalAmount
  type: number
- description: Invoice currency code
  name: currency
  type: string
- description: Invoice payment status
  name: status
  type: string
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/billing-invoice-schema.json
slug: billing-invoice
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: Invoice
---
