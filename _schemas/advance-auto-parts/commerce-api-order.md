---
description: A placed order.
layout: schema
name: Order
properties_list:
- description: Order identifier.
  name: id
  type: string
- description: Current order status.
  name: status
  type: string
- description: Order total.
  name: total
  type: number
- description: Order creation timestamp.
  name: createdAt
  type: string
- description: Items in the order.
  name: items
  type: array
provider_name: Advance Auto Parts
provider_slug: advance-auto-parts
schema_file: json-schema/commerce-api-order-schema.json
slug: commerce-api-order
tags:
- Automotive
- E-Commerce
- Parts Catalog
- Retail
- Supply Chain
title: Order
---
