---
description: A gas supply order to Air Products
layout: schema
name: GasOrder
properties_list:
- description: Order identifier
  name: order_id
  type: string
- description: Customer account number
  name: customer_id
  type: string
- description: Product ordered
  name: product_id
  type: string
- description: Quantity ordered in specified unit
  name: quantity
  type: number
- description: Unit of measure (SCF, kg, liters)
  name: unit
  type: string
- description: Requested delivery date
  name: delivery_date
  type: string
- description: Delivery site address
  name: delivery_address
  type: string
- description: Order status
  name: status
  type: string
provider_name: Air Products and Chemicals
provider_slug: air-products-and-chemicals
schema_file: json-schema/airproducts-gas-order-schema.json
slug: airproducts-gas-order
tags:
- Industrial Gases
- Chemicals
- Energy
- Manufacturing
- Hydrogen
- Enterprise
title: GasOrder
---
