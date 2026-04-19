---
description: A single fundamental data point representing a metric value for a specific security, fiscal period, and periodicity.
layout: schema
name: Fundamental
properties_list:
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: FactSet Regional Security Identifier. Six alpha-numeric characters, excluding vowels, with an -R suffix (XXXXXX-R).
  name: fsymId
  type: '[''string'', ''null'']'
- description: The requested metric input, representing the Fundamental Data Item.
  name: metric
  type: '[''string'', ''null'']'
- description: Periodicity or frequency of the fiscal periods.
  name: periodicity
  type: '[''string'', ''null'']'
- description: 'Fiscal period indicator. QUARTERLY: 1-4, SEMI-ANNUAL: 1-2, ANNUAL: 0.'
  name: fiscalPeriod
  type: '[''integer'', ''null'']'
- description: Fiscal year of the reported period in YYYY format.
  name: fiscalYear
  type: '[''integer'', ''null'']'
- description: Length of the fiscal period in days.
  name: fiscalPeriodLength
  type: '[''integer'', ''null'']'
- description: The normalized date the fiscal period ended in YYYY-MM-DD format.
  name: fiscalEndDate
  type: '[''string'', ''null'']'
- description: The date the reported fiscal period ended.
  name: reportDate
  type: '[''string'', ''null'']'
- description: The date the EPS was reported for the requested periodicity.
  name: epsReportDate
  type: '[''string'', ''null'']'
- description: Update type. Preliminary indicates limited data; Final indicates full financial statement data.
  name: updateType
  type: '[''string'', ''null'']'
- description: ISO 4217 currency code for the data values.
  name: currency
  type: '[''string'', ''null'']'
- description: Value of the data metric requested. The type varies depending on the metric - may be a number (double) or string.
  name: value
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-fundamentals-fundamental-schema.json
slug: factset-fundamentals-fundamental
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Fundamental
---
