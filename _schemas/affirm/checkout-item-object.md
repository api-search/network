---
description: Represents a single line item in the checkout, including product details and pricing.
layout: schema
name: ItemObject
properties_list:
- description: Customer-facing product name.
  name: display_name
  type: string
- description: Merchant's stock keeping unit identifier for the product.
  name: sku
  type: string
- description: Unit price of the item in cents.
  name: unit_price
  type: integer
- description: Quantity of this item in the order.
  name: qty
  type: integer
- description: URL of the product image.
  name: item_image_url
  type: string
- description: URL of the product page on the merchant's website.
  name: item_url
  type: string
- description: Nested array of category strings representing the product taxonomy.
  name: categories
  type: array
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/checkout-item-object-schema.json
slug: checkout-item-object
tags: []
title: ItemObject
---
