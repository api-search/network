---
description: Writable fields for creating a new query
layout: schema
name: WriteQuery
properties_list:
- description: LookML model name
  name: model
  type: string
- description: LookML explore (view) name
  name: view
  type: string
- description: List of field names to include
  name: fields
  type: array
- description: Fields to pivot on
  name: pivots
  type: array
- description: Fields to fill missing values for
  name: fill_fields
  type: array
- description: Filter expressions keyed by field name
  name: filters
  type: object
- description: Custom filter expression
  name: filter_expression
  type: string
- description: Sort order for results
  name: sorts
  type: array
- description: Maximum rows to return
  name: limit
  type: string
- description: Maximum columns for pivoted results
  name: column_limit
  type: string
- description: Include row totals
  name: total
  type: boolean
- description: Row total setting
  name: row_total
  type: string
- description: Fields to subtotal on
  name: subtotals
  type: array
- description: JSON string of dynamic field definitions
  name: dynamic_fields
  type: string
- description: Visualization configuration
  name: vis_config
  type: object
- description: Timezone for date/time calculations
  name: query_timezone
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-write-query-schema.json
slug: looker-write-query
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: WriteQuery
---
