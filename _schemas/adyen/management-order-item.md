---
description: OrderItem schema from Adyen API
layout: schema
name: OrderItem
properties_list:
- description: The unique identifier of the product.
  name: id
  type: string
- description: The number of installments for the specified product `id`.
  name: installments
  type: integer
- description: The name of the product.
  name: name
  type: string
- description: The number of items with the specified product `id` included in the order.
  name: quantity
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-order-item-schema.json
slug: management-order-item
tags:
- Payments
- Financial Services
- Fintech
title: OrderItem
---
