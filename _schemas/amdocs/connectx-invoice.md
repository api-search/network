---
description: Invoice schema from Amdocs API
layout: schema
name: Invoice
properties_list:
- description: ''
  name: invoiceId
  type: string
- description: ''
  name: invoiceNumber
  type: string
- description: ''
  name: customerId
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: invoiceDate
  type: string
- description: ''
  name: dueDate
  type: string
- description: ''
  name: totalAmount
  type: number
- description: ''
  name: taxAmount
  type: number
- description: ''
  name: currency
  type: string
- description: ''
  name: lineItems
  type: array
provider_name: Amdocs
provider_slug: amdocs
schema_file: json-schema/connectx-invoice-schema.json
slug: connectx-invoice
tags:
- Telecom
- BSS
- OSS
- Billing
- Customer Management
- MVNO
- 5G
- SaaS
title: Invoice
---
