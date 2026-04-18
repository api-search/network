---
description: An invoice from a connected accounting system in the Merge Unified API.
layout: schema
name: Invoice
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: remote_id
  type: string
- description: ''
  name: type
  type: string
- description: ''
  name: contact
  type: string
- description: Invoice number.
  name: number
  type: string
- description: ''
  name: issue_date
  type: string
- description: ''
  name: due_date
  type: string
- description: ''
  name: paid_on_date
  type: string
- description: ''
  name: memo
  type: string
- description: ISO 4217 currency code.
  name: currency
  type: string
- description: ''
  name: total_discount
  type: number
- description: ''
  name: sub_total
  type: number
- description: ''
  name: total_tax_amount
  type: number
- description: ''
  name: total_amount
  type: number
- description: ''
  name: balance
  type: number
- description: ''
  name: status
  type: string
- description: ''
  name: line_items
  type: array
- description: ''
  name: remote_was_deleted
  type: boolean
provider_name: Merge
provider_slug: merge
schema_file: json-schema/accounting-api-invoice-schema.json
slug: accounting-api-invoice
tags:
- Integrations
- Platform
- Unified API
title: Invoice
---
