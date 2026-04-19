---
description: ''
layout: schema
name: PACalculationParameters
properties_list:
- description: The PA Engine component identifier to analyze.
  name: componentid
  type: string
- description: List of accounts.
  name: accounts
  type: array
- description: List of benchmarks.
  name: benchmarks
  type: array
- description: List of groupings for the PA calculation. This will take precedence over the groupings saved in the PA document.
  name: groups
  type: array
- description: Currency ISO code for calculation.
  name: currencyisocode
  type: string
- description: List of columns for the PA calculation. This will take precedence over the columns saved in the PA document.
  name: columns
  type: array
- description: Component detail type for the PA component. It can be GROUPS or GROUPSALL or TOTALS or SECURITIES.
  name: componentdetail
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-pa-engine-pa-calculation-parameters-schema.json
slug: factset-pa-engine-pa-calculation-parameters
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: PACalculationParameters
---
