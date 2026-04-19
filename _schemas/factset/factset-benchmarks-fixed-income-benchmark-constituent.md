---
description: ''
layout: schema
name: fixedIncomeBenchmarkConstituent
properties_list:
- description: Benchmark Id
  name: fsymId
  type: string
- description: Date of weight and shares.
  name: date
  type: string
- description: FactSet Security Identifier (-S).
  name: fsymSecurityId
  type: string
- description: Weight of Security in benchmark (percent).
  name: weightClose
  type: number
- description: Amount Outstanding for the Fixed Income Security.
  name: amountOutstanding
  type: number
- description: Fixed Income Price of security held.
  name: price
  type: number
- description: Market value adjusted. Market Value represented in Millions.
  name: adjMarketValue
  type: number
- description: Identifier specified in the request
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-benchmarks-fixed-income-benchmark-constituent-schema.json
slug: factset-benchmarks-fixed-income-benchmark-constituent
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: fixedIncomeBenchmarkConstituent
---
