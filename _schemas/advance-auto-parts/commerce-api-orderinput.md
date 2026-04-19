---
description: Request to create a new order.
layout: schema
name: OrderInput
properties_list:
- description: Cart to convert to an order.
  name: cartId
  type: string
- description: Store for pickup.
  name: storeId
  type: string
- description: Fulfillment type.
  name: fulfillmentType
  type: string
- description: Payment method identifier.
  name: paymentMethodId
  type: string
provider_name: Advance Auto Parts
provider_slug: advance-auto-parts
schema_file: json-schema/commerce-api-orderinput-schema.json
slug: commerce-api-orderinput
tags:
- Automotive
- E-Commerce
- Parts Catalog
- Retail
- Supply Chain
title: OrderInput
---
