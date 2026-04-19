---
description: ''
layout: schema
name: highLow
properties_list:
- description: Date of last split for which prices have been adjusted.
  name: adjDate
  type: string
- description: Specific reference date for the period expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: The period of measure requested using the period query parameter.
  name: period
  type: string
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: High price over the period requested. This can represent the intra-day or closing price depending on the priceType requested. By default the price is as of closing in local trading currency, split adj
  name: priceHigh
  type: number
- description: Low price over the period requested. This can represent the intra-day or closing price depending on the priceType requested. By default the price is as of closing in local trading currency, split adju
  name: priceLow
  type: number
- description: Date in which the highest price occurred over the requested period for the given id expressed in YYYY-MM-DD format.
  name: priceHighDate
  type: string
- description: Date in which the lowest price occurred over the requested period for the given id expressed in YYYY-MM-DD format.
  name: priceLowDate
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-high-low-schema.json
slug: factset-prices-high-low
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: highLow
---
