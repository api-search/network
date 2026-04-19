---
description: Returns Coverage Response of the requested ticker with unique isocode within a date range
layout: schema
name: coverageTickHistory
properties_list:
- description: a unique ticker given to a company
  name: ticker
  type: string
- description: FactSet specific exchange code.
  name: factsetExchangeCode
  type: string
- description: The date for (or from which) the coverage is required.
  name: startDate
  type: string
- description: This specifies the latest traded date from tick history.
  name: latestTradeDate
  type: string
- description: Name of the firm
  name: companyName
  type: string
- description: returns the ISIN of the requested company
  name: isin
  type: string
- description: Represents 3 digit ISO code for the currency
  name: currency
  type: string
- description: the last traded exhange code from tick history
  name: lastExchangeCode
  type: string
- description: the last traded exchange name from tick history
  name: lastExchangeName
  type: string
- description: the primary ticker iso
  name: primaryTickerExchange
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-tick-history-coverage-tick-history-schema.json
slug: factset-tick-history-coverage-tick-history
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: coverageTickHistory
---
