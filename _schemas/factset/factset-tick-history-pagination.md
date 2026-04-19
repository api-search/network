---
description: List of pagination objects
layout: schema
name: pagination
properties_list:
- description: Total number of files the API returns for a particular query
  name: total
  type: integer
- description: Boolean value that represents whether the total count of files returned is exact or an estimate. This is defaulted to False as the API should always return the exact count
  name: isEstimatedTotal
  type: boolean
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-tick-history-pagination-schema.json
slug: factset-tick-history-pagination
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: pagination
---
