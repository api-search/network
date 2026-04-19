---
description: ''
layout: schema
name: indexSnapshot
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
- description: Currency Code used in adjustments. If no Currency was requested, the service will default to the local Calendar.
  name: currency
  type: string
- description: Index Level Market Capitalization as of the date requested expressed in millions.
  name: marketValue
  type: number
- description: Index Level Price
  name: price
  type: number
- description: Index Level Price - 1 Day percent change
  name: priceReturnPercent1D
  type: number
- description: Index Level Price - Quarter-to-Date percent change
  name: priceReturnPercentQTD
  type: number
- description: Index Level Price - Year-to-Date percent change
  name: priceReturnPercentYTD
  type: number
- description: Index Level Total Return Amount. (Gross or Net depends on requested returnType)
  name: totalReturnLevel
  type: number
- description: Index Level Total Return - 1 Day percent change. (Gross or Net depends on requested returnType)
  name: totalReturnPercent1D
  type: number
- description: Index Level Total Return - Quarter-to-Date percent change. (Gross or Net depends on requested returnType)
  name: totalReturnPercentQTD
  type: number
- description: Index Level Total Return - Year-to-Date percent change. (Gross or Net depends on requested returnType)
  name: totalReturnPercentYTD
  type: number
- description: The requested Return Type - GROSS or NET
  name: returnType
  type: string
- description: Benchmark Identifier specified in the request
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-benchmarks-index-snapshot-schema.json
slug: factset-benchmarks-index-snapshot
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: indexSnapshot
---
