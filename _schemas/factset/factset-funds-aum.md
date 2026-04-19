---
description: ''
layout: schema
name: aum
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: Returns fund-level Assets Under Management (AUM) data. Fund-level AUM is the sum of the market values of the positions in the fund's portfolio. This represents all share classes.
  name: fundLevelAUM
  type: number
- description: 'As-Reported AUM. Calculated by using shares outstanding at previous close multiplied by NAV at previous close. This is typically the value seen on fund websites. As Reported AUM = (Shares Outstanding '
  name: shrClassAUMRpt
  type: number
- description: 'Actual AUM. Calculated by using shares outstanding at previous close multiplied by NAV of one day prior to close. This is the value used in calculating fund flows. Actual AUM = (Shares Outstanding t0 '
  name: shrClassAUMAct
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
schema_file: json-schema/factset-funds-aum-schema.json
slug: factset-funds-aum
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: aum
---
