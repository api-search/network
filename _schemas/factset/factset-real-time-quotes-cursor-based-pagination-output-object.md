---
description: Pagination attributes for the cursor-based pagination strategy.
layout: schema
name: CursorBasedPaginationOutputObject
properties_list:
- description: Total number of entries in the result set.
  name: total
  type: number
- description: Flag indicating that the value of `total` is estimated.
  name: isEstimatedTotal
  type: boolean
- description: The next cursor position to use in the parameter `pagination.cursor` for an endpoint that supports cursor-based pagination, otherwise `null`.
  name: next
  type: string
- description: 'The previous cursor position to use in the parameter `pagination.cursor` for an endpoint that supports cursor-based pagination. If a previous cursor position is not supported or available, `previous` '
  name: previous
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-real-time-quotes-cursor-based-pagination-output-object-schema.json
slug: factset-real-time-quotes-cursor-based-pagination-output-object
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: CursorBasedPaginationOutputObject
---
