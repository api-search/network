---
description: Results from an Aladdin Data Cloud query execution
layout: schema
name: QueryResult
properties_list:
- description: Unique query execution identifier
  name: queryId
  type: string
- description: Query execution status
  name: status
  type: string
- description: Number of rows returned
  name: rowCount
  type: integer
- description: Column definitions
  name: columns
  type: array
- description: Result rows as arrays
  name: rows
  type: array
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-data-cloud-query-result-schema.json
slug: aladdin-studio-data-cloud-query-result
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: QueryResult
---
