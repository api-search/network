---
description: An automotive part or product.
layout: schema
name: Product
properties_list:
- description: Product SKU.
  name: id
  type: string
- description: Product name.
  name: name
  type: string
- description: Manufacturer part number.
  name: partNumber
  type: string
- description: Brand name.
  name: brand
  type: string
- description: Product description.
  name: description
  type: string
- description: Current retail price.
  name: price
  type: number
- description: Whether available.
  name: available
  type: boolean
- description: Product category identifier.
  name: categoryId
  type: string
provider_name: Advance Auto Parts
provider_slug: advance-auto-parts
schema_file: json-schema/catalog-api-product-schema.json
slug: catalog-api-product
tags:
- Automotive
- E-Commerce
- Parts Catalog
- Retail
- Supply Chain
title: Product
---
