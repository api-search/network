---
description: ''
layout: schema
name: flows
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: Fund flows data for the specified share class in raw units of the specified currency.
  name: fundFlows
  type: number
- description: The Currency of the AUM values. By default it will be in the FUnds Currency, unless otherwise requested via the currency parameter.
  name: currency
  type: string
- description: The date of the AUM in YYYY-MM-DD format.
  name: date
  type: string
- description: The requested Id sent as input.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-flows-schema.json
slug: factset-funds-flows
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: flows
---
