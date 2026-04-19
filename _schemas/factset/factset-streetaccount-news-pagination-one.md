---
description: List of pagination objects
layout: schema
name: paginationOne
properties_list:
- description: Total number of files the API returns for a particular query
  name: total
  type: integer
- description: Boolean value that represents whether the total count of files returned is exact or an estimate. This is defaulted to False as the API should always return the exact count
  name: isEstimatedTotal
  type: boolean
- description: Number of results returned per page
  name: limit
  type: integer
- description: The flag indicating the position in the results array if additional results are available beyond the default value or the value in paginationLimit parameter (if used). This value is passed in the _pag
  name: offset
  type: integer
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-streetaccount-news-pagination-one-schema.json
slug: factset-streetaccount-news-pagination-one
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: paginationOne
---
