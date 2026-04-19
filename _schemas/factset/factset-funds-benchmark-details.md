---
description: ''
layout: schema
name: benchmarkDetails
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: The Fund's primary Benchmark Identifier.
  name: benchmarkId
  type: string
- description: The proper name of the Benchmark Id.
  name: benchmarkName
  type: string
- description: Indicates if the Fund has a composite benchmark.
  name: multipleBenchmarkFlag
  type: string
- description: The date in which the benchmark changed for the requested fund in YYYY-MM-DD. If no benchmark changes occurred, the response value will be null.
  name: benchmarkChangeDate
  type: string
- description: The segment of the respective segment benchmark id.
  name: segment
  type: string
- description: Segment Benchmark Identifier. Funds in the same segment match on all seven levels of FactSet's fund classification system.
  name: segmentBenchmarkId
  type: string
- description: The segment benchmark's name in proper format. Funds in the same segment match on all seven levels of FactSet's fund classification system.
  name: segmentBenchmarkName
  type: string
- description: The Segment Benchmark's currency in ISO3. Funds in the same segment match on all seven levels of FactSet's fund classification system.
  name: segmentBenchmarkCurrency
  type: string
- description: The Segment benchmarks return type. Funds in the same segment match on all seven levels of FactSet's fund classification system.
  name: segmentBenchmarkReturnType
  type: string
- description: The requested Id sent as input.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-benchmark-details-schema.json
slug: factset-funds-benchmark-details
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: benchmarkDetails
---
