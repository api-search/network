---
description: ''
layout: schema
name: NumericBoost
properties_list:
- description: Weight to apply for boosting this numerical column. It will be normalized across all scored columns specified in the scoring config so that all weights sum to 1. If a weight is not provided, the weigh
  name: weight
  type: number
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-search-service-numeric-boost-schema.json
slug: cortex-search-service-numeric-boost
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: NumericBoost
---
