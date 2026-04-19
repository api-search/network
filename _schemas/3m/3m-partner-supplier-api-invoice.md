---
description: An invoice issued by 3M for an order
layout: schema
name: Invoice
properties_list:
- description: Unique invoice identifier
  name: invoiceId
  type: string
- description: Associated order identifier
  name: orderId
  type: string
- description: Date the invoice was issued
  name: invoiceDate
  type: string
- description: Payment due date
  name: dueDate
  type: string
- description: Total invoice amount
  name: totalAmount
  type: number
- description: Currency code (ISO 4217)
  name: currency
  type: string
- description: Invoice payment status
  name: status
  type: string
provider_name: 3M
provider_slug: 3m
schema_file: json-schema/3m-partner-supplier-api-invoice-schema.json
slug: 3m-partner-supplier-api-invoice
tags:
- Industrial
- Manufacturing
- Supply Chain
title: Invoice
---
