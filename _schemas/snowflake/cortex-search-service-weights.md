---
description: Weights to apply to each scoring component.
layout: schema
name: Weights
properties_list:
- description: Weight to apply to all text-specific columns.
  name: texts
  type: number
- description: Weight to apply to all vector-specific columns.
  name: vectors
  type: number
- description: Weight to apply to reranker-specific scoring component.
  name: reranker
  type: number
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-search-service-weights-schema.json
slug: cortex-search-service-weights
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Weights
---
