---
description: LineItem schema from Adyen API
layout: schema
name: LineItem
properties_list:
- description: Item amount excluding the tax, in minor units.
  name: amountExcludingTax
  type: integer
- description: Item amount including the tax, in minor units.
  name: amountIncludingTax
  type: integer
- description: Brand of the item.
  name: brand
  type: string
- description: Color of the item.
  name: color
  type: string
- description: Description of the line item.
  name: description
  type: string
- description: ID of the line item.
  name: id
  type: string
- description: Link to the picture of the purchased item.
  name: imageUrl
  type: string
- description: Item category, used by the payment methods PayPal and Ratepay.
  name: itemCategory
  type: string
- description: Manufacturer of the item.
  name: manufacturer
  type: string
- description: Link to the purchased item.
  name: productUrl
  type: string
- description: Number of items.
  name: quantity
  type: integer
- description: Email associated with the given product in the basket (usually in electronic gift cards).
  name: receiverEmail
  type: string
- description: Size of the item.
  name: size
  type: string
- description: Stock keeping unit.
  name: sku
  type: string
- description: Tax amount, in minor units.
  name: taxAmount
  type: integer
- description: Tax percentage, in minor units.
  name: taxPercentage
  type: integer
- description: Universal Product Code.
  name: upc
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-line-item-schema.json
slug: checkout-line-item
tags:
- Payments
- Financial Services
- Fintech
title: LineItem
---
