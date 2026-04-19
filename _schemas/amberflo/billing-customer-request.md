---
description: Request body for creating or updating a customer
layout: schema
name: CustomerRequest
properties_list:
- description: Unique customer identifier
  name: customerId
  type: string
- description: Customer display name
  name: customerName
  type: string
- description: Customer email address
  name: customerEmail
  type: string
- description: Customer description
  name: description
  type: string
- description: Marks customer as test
  name: test
  type: boolean
- description: Lifecycle stage
  name: lifecycleStage
  type: string
- description: Custom metadata
  name: traits
  type: object
- description: ''
  name: address
  type: object
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/billing-customer-request-schema.json
slug: billing-customer-request
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: CustomerRequest
---
