---
description: ''
layout: schema
name: marketValue
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: Ending date for the period expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: 'Currency ISO code. For more details, visit [Online Assistant Page #1470](https://oa.apps.factset.com/pages/1470).'
  name: currency
  type: string
- description: Aggregate market value across all share classes and includes non-traded shares which are added to the calculation basis by the proportion of their nominal or par value. Values are in base units. To va
  name: entityMarketValue
  type: number
- description: 'Aggregate across all share classes and excludes non-traded shares. Values are in base units. For more details visit [Online Assistant Page #16867](https://my.apps.factset.com/oa/pages/16867).'
  name: entityMarketValueExNonTraded
  type: number
- description: Returns the security level market value calculated as the share price multiplied by the number of shares at the security level. **Note:** History is available back to Oct-1999 for North American secur
  name: securityMarketValue
  type: number
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-market-value-schema.json
slug: factset-prices-market-value
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: marketValue
---
