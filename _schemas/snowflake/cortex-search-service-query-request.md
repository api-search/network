---
description: A search query and additional parameters for search.
layout: schema
name: QueryRequest
properties_list:
- description: Unstructured text query. Exactly one of 'query' or 'multi_index_query' must be specified.
  name: query
  type: string
- description: A search query expressed as a collection of multiple column-level queries. Exactly one of 'query' or 'multi_index_query' must be specified. A column/index can be queried with multiple queries.
  name: multi_index_query
  type: object
- description: List of columns to return.
  name: columns
  type: array
- description: Filter query.
  name: filter
  type: object
- description: Max number of results to return.
  name: limit
  type: integer
- description: reserved
  name: experimental
  type: object
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-search-service-query-request-schema.json
slug: cortex-search-service-query-request
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: QueryRequest
---
