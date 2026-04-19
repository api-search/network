---
description: A single consensus estimate data point aggregating analyst projections for a security, metric, and fiscal period.
layout: schema
name: Estimate
properties_list:
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: FactSet Regional Security Identifier.
  name: fsymId
  type: '[''string'', ''null'']'
- description: The estimate metric identifier.
  name: metric
  type: '[''string'', ''null'']'
- description: Periodicity of the fiscal period.
  name: periodicity
  type: '[''string'', ''null'']'
- description: Fiscal period indicator.
  name: fiscalPeriod
  type: '[''integer'', ''null'']'
- description: Fiscal year in YYYY format.
  name: fiscalYear
  type: '[''integer'', ''null'']'
- description: The date the fiscal period ends.
  name: fiscalEndDate
  type: '[''string'', ''null'']'
- description: ISO 4217 currency code.
  name: currency
  type: '[''string'', ''null'']'
- description: Number of analyst estimates included in the consensus.
  name: estimateCount
  type: '[''integer'', ''null'']'
- description: Mean (average) of analyst estimates.
  name: mean
  type: '[''number'', ''null'']'
- description: Median of analyst estimates.
  name: median
  type: '[''number'', ''null'']'
- description: Highest analyst estimate.
  name: high
  type: '[''number'', ''null'']'
- description: Lowest analyst estimate.
  name: low
  type: '[''number'', ''null'']'
- description: Standard deviation of analyst estimates.
  name: standardDeviation
  type: '[''number'', ''null'']'
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-fundamentals-estimate-schema.json
slug: factset-fundamentals-estimate
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Estimate
---
