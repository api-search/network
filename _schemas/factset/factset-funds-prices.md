---
description: ''
layout: schema
name: prices
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: The NAV for the requested share class. NOTE - FactSet Mutual Funds does not use seven-day yields to price money market funds.
  name: price
  type: number
- description: The date of the NAV in YYYY-MM-DD format.
  name: date
  type: string
- description: The requested Id sent as input.
  name: requestId
  type: string
- description: ISO3 Currency
  name: currency
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-prices-schema.json
slug: factset-funds-prices
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: prices
---
