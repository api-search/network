---
description: ''
layout: schema
name: annualizedDividendsObject
properties_list:
- description: Factset Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R). Identifies the security's best regional security data series per currency. For equit
  name: fsymId
  type: string
- description: FactSet identifier that uniquely identifies the Event.
  name: eventId
  type: string
- description: Effective Date or Ex-Date of Annualized Dividend in YYYY-MM-DD format.
  name: effectiveDate
  type: string
- description: Annualized Dividend value in the trading currency. The value is adjusted for splits
  name: iadDefTradingAdj
  type: number
- description: 'Currency ISO code associated with the annualized dividends.For more details, visit [Online Assistant Page #1470](https://oa.apps.factset.com/pages/1470).'
  name: currency
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-global-prices-annualized-dividends-object-schema.json
slug: factset-global-prices-annualized-dividends-object
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: annualizedDividendsObject
---
