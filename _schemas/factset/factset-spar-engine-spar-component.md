---
description: ''
layout: schema
name: SPARComponent
properties_list:
- description: Component identifier.
  name: id
  type: string
- description: List of accounts in SPAR document.
  name: accounts
  type: array
- description: CurrencyCode in SPAR document.
  name: currencyIsoCode
  type: string
- description: The path to the document
  name: path
  type: string
- description: Component name.
  name: name
  type: string
- description: Component category.
  name: category
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-spar-engine-spar-component-schema.json
slug: factset-spar-engine-spar-component
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: SPARComponent
---
