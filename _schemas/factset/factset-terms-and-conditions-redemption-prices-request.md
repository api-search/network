---
description: ''
layout: schema
name: redemptionPricesRequest
properties_list:
- description: List of Fixed Income Security identifiers. Supported symbol types include CUSIP, SEDOL, ISIN, and FactSet Security Permanent Identifier (-S). **ID LIMIT = 250** *per request*.
  name: ids
  type: array
- description: Filters the list of Redemption Prices Categories - * **CALL** = Call prices. * **PUT** = Put prices. * **SF** = Sinking Fund prices.
  name: categories
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-redemption-prices-request-schema.json
slug: factset-terms-and-conditions-redemption-prices-request
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: redemptionPricesRequest
---
