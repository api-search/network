---
description: Query execution result.
layout: schema
name: QueryResult
properties_list:
- description: Unique query identifier.
  name: queryId
  type: string
- description: Query execution status.
  name: status
  type: string
- description: Number of rows returned.
  name: rowCount
  type: integer
- description: Column metadata.
  name: columns
  type: array
- description: Result rows.
  name: rows
  type: array
- description: Error message if query failed.
  name: errorMessage
  type: string
provider_name: Teradata
provider_slug: teradata
schema_file: json-schema/query-service-api-query-result-schema.json
slug: query-service-api-query-result
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
title: QueryResult
---
