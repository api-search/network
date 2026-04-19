---
description: JSON Schema for an Amdocs BSS telecom customer account.
layout: schema
name: Amdocs Customer
properties_list:
- description: Unique customer identifier
  name: customerId
  type: string
- description: Classification of the customer
  name: customerType
  type: string
- description: ''
  name: status
  type: string
- description: Customer-facing account number
  name: accountNumber
  type: string
- description: ''
  name: firstName
  type: string
- description: ''
  name: lastName
  type: string
- description: Company name for Business/Government customers
  name: companyName
  type: string
- description: ''
  name: email
  type: string
- description: ''
  name: phone
  type: string
- description: ''
  name: address
  type: object
- description: ''
  name: billingAddress
  type: object
- description: ''
  name: subscriptions
  type: array
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
provider_name: Amdocs
provider_slug: amdocs
schema_file: json-schema/amdocs-customer-schema.json
slug: amdocs-customer
tags:
- Telecom
- BSS
- OSS
- Billing
- Customer Management
- MVNO
- 5G
- SaaS
title: Amdocs Customer
---
