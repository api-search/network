---
description: ''
layout: schema
name: indexHistory
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
- description: The total number of constituents as of the date requested.
  name: constituentNumber
  type: integer
- description: Currency Code used in adjustments. If no Currency was requested, the service will default to LOCAL ('LOC').
  name: currency
  type: string
- description: Index Level Market Capitalization as of the date requested expressed in millions.
  name: marketValue
  type: number
- description: Index Level Price
  name: price
  type: number
- description: Index Level Price Percent Change
  name: priceReturnPercent
  type: number
- description: Index Level Total Return Amount
  name: totalReturnLevel
  type: number
- description: Index Level Total Return Percent Change
  name: totalReturnPercent
  type: number
- description: The requested Return Type - GROSS or NET
  name: returnType
  type: string
- description: The requested Hedge Type - HEDGED or UNHEDGED
  name: hedgeType
  type: string
- description: Benchmark Identifier specified in the request
  name: requestId
  type: string
- description: This field will always return the date of the data that was actually returned.
  name: observationDate
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-benchmarks-index-history-schema.json
slug: factset-benchmarks-index-history
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: indexHistory
---
