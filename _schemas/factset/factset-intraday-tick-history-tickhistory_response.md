---
description: response for tick history
layout: schema
name: tickhistory_response
properties_list:
- description: Request Identification String.
  name: Requested ID
  type: string
- description: Single Requested Symbol or Security.
  name: Requested Symbol
  type: string
- description: Array of requested fields
  name: Requested Fields
  type: array
- description: ''
  name: Request Key
  type: string
- description: ''
  name: Error Code
  type: string
- description: Brief description of error response. Blank if successful.
  name: Error Description
  type: string
- description: Requested Field Names
  name: Field Names
  type: string
- description: Requested Field ID numbers 'FID'. Found in Data Service Manual.
  name: Field IDs
  type: number
- description: Requested Symbol Key, where :D represented delayed data.
  name: Key
  type: string
- description: Array of field values. Each value is returned for requested interval query.
  name: Values
  type: number
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-intraday-tick-history-tickhistory_response-schema.json
slug: factset-intraday-tick-history-tickhistory_response
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: tickhistory_response
---
