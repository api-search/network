---
description: An Airgas B2B customer order for industrial gases, welding, or safety products.
layout: schema
name: Order
properties_list:
- description: Unique order number.
  name: order_number
  type: string
- description: Customer account number.
  name: account_number
  type: string
- description: Current order status.
  name: status
  type: string
- description: Date and time the order was placed.
  name: order_date
  type: string
- description: Scheduled or actual delivery date.
  name: delivery_date
  type: string
- description: Customer purchase order number.
  name: purchase_order
  type: string
- description: Delivery address for the order.
  name: delivery_address
  type: object
- description: Products included in the order.
  name: line_items
  type: array
- description: Total order amount.
  name: total_amount
  type: number
provider_name: Airgas
provider_slug: airgas
schema_file: json-schema/airgas-order-schema.json
slug: airgas-order
tags:
- Industrial Gases
- Welding
- Safety
- B2B
- Supply Chain
- Manufacturing
- Healthcare
title: Order
---
