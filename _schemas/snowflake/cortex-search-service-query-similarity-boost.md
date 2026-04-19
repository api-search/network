---
description: ''
layout: schema
name: QuerySimilarityBoost
properties_list:
- description: Fully-qualified name of a Cortex Search Service through which to find similar previous queries.
  name: cortex_search_service
  type: string
- description: Name of a TEXT column indexed in the specified previous queries search service that contains the previous query strings.
  name: previous_query_column
  type: string
- description: Name of an ARRAY column indexed in the specified previous queries search service that contains a list of documents that matched the corresponding previous query. Each document is represented as an OBJ
  name: documents_column
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-search-service-query-similarity-boost-schema.json
slug: cortex-search-service-query-similarity-boost
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: QuerySimilarityBoost
---
