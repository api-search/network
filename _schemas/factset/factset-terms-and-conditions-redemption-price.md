---
description: Redemption Price Data Items for a Fixed Income security.
layout: schema
name: redemptionPrice
properties_list:
- description: Security identifier used in the request.
  name: requestId
  type: string
- description: FactSet Permanent Security Identifier.
  name: fsymId
  type: string
- description: Date of the Redemption Price.
  name: date
  type: string
- description: Redemption Price Category - * **CALL** = Call prices. * **PUT** = Put prices. * **SF** = Sinking Fund prices.
  name: category
  type: string
- description: Sinking Fund minimum amount.
  name: minAmt
  type: number
- description: Redemption price for the category.
  name: price
  type: number
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-redemption-price-schema.json
slug: factset-terms-and-conditions-redemption-price
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: redemptionPrice
---
