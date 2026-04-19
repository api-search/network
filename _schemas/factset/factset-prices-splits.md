---
description: ''
layout: schema
name: splits
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: Ex-Date of the split expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: Split adjustment factor for n splits ago. A 2-for-1 split returns .50, the number you would multiply the stock price by to adjust for the split.
  name: splitFactor
  type: number
- description: Description for the type of split or spin off.
  name: splitComment
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-splits-schema.json
slug: factset-prices-splits
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: splits
---
