---
description: Pricing information for a specific 3M product
layout: schema
name: ProductPrice
properties_list:
- description: Unique product identifier
  name: productId
  type: string
- description: Partner-negotiated unit price
  name: unitPrice
  type: number
- description: Currency code (ISO 4217)
  name: currency
  type: string
- description: Pricing tier applied to this partner
  name: pricingTier
  type: string
- description: Date when this pricing becomes effective
  name: effectiveDate
  type: string
- description: Date when this pricing expires
  name: expirationDate
  type: string
provider_name: 3M
provider_slug: 3m
schema_file: json-schema/3m-partner-supplier-api-product-price-schema.json
slug: 3m-partner-supplier-api-product-price
tags:
- Industrial
- Manufacturing
- Supply Chain
title: ProductPrice
---
