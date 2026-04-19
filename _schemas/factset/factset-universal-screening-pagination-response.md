---
description: ''
layout: schema
name: PaginationResponse
properties_list:
- description: Denotes if the 'total' property is an estimation
  name: isEstimatedTotal
  type: boolean
- description: Next cursor to be sent, will be null when there are no more results
  name: next
  type: string
- description: Previous cursor, currently not supported
  name: prev
  type: integer
- description: Total number of rows in the screen
  name: total
  type: integer
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-universal-screening-pagination-response-schema.json
slug: factset-universal-screening-pagination-response
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: PaginationResponse
---
