---
description: ''
layout: schema
name: benchmarkRatios
properties_list:
- description: Requested Identifier. Must be a valid Benchmark Identifier recognized by FactSet.
  name: fsymId
  type: string
- description: The respective date for values as of the date requested in YYYY-MM-DD format.
  name: date
  type: string
- description: Proper Name of Index.
  name: name
  type: string
- description: Benchmark Identifier specified in the request.
  name: requestId
  type: string
- description: Metric requested
  name: metric
  type: string
- description: The periodicity submitted in the request.
  name: periodicity
  type: string
- description: The currency submitted in the request.
  name: currency
  type: string
- description: Ratio value based on the metric requested.
  name: value
  type: number
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-benchmarks-benchmark-ratios-schema.json
slug: factset-benchmarks-benchmark-ratios
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: benchmarkRatios
---
