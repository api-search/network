---
description: Query specification of a given column. Exactly one of 'text' or 'vector' must be specified.
layout: schema
name: ColumnQuery
properties_list:
- description: Unstructured text query for querying a text index.
  name: text
  type: string
- description: Query embedding vector. Must be computed using the same model as used for embedding the column being queried.
  name: vector
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-search-service-column-query-schema.json
slug: cortex-search-service-column-query
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ColumnQuery
---
