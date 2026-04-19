---
description: A customer account in Amberflo
layout: schema
name: Customer
properties_list:
- description: Creation timestamp in Unix milliseconds
  name: createTime
  type: integer
- description: Last update timestamp in Unix milliseconds
  name: updateTime
  type: integer
- description: Deletion timestamp in Unix milliseconds
  name: deleteTime
  type: integer
- description: Unique customer identifier from your system
  name: customerId
  type: string
- description: Customer display name
  name: customerName
  type: string
- description: Customer contact email
  name: customerEmail
  type: string
- description: Customer description
  name: description
  type: string
- description: Deprecated — use lifecycleStage instead
  name: enabled
  type: boolean
- description: Whether this is a test customer account
  name: test
  type: boolean
- description: Customer lifecycle stage
  name: lifecycleStage
  type: string
- description: Last deactivation timestamp in Unix milliseconds
  name: deactivateTimeStamp
  type: integer
- description: Custom metadata for external system integration
  name: traits
  type: object
- description: ''
  name: address
  type: object
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/billing-customer-schema.json
slug: billing-customer
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: Customer
---
