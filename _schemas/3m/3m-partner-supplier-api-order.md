---
description: A purchase order placed with 3M
layout: schema
name: Order
properties_list:
- description: Unique order identifier
  name: orderId
  type: string
- description: Current order status
  name: status
  type: string
- description: Order creation timestamp
  name: createdAt
  type: string
- description: Total order value
  name: totalAmount
  type: number
- description: Currency code (ISO 4217)
  name: currency
  type: string
- description: Line items in the order
  name: items
  type: array
provider_name: 3M
provider_slug: 3m
schema_file: json-schema/3m-partner-supplier-api-order-schema.json
slug: 3m-partner-supplier-api-order
tags:
- Industrial
- Manufacturing
- Supply Chain
title: Order
---
