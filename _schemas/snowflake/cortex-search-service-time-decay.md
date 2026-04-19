---
description: ''
layout: schema
name: TimeDecay
properties_list:
- description: Weight to apply for decaying this timestamp column. Normalized across all scored columns in the scoring config so that all weights sum to 1. If a weight is not provided, the weight defaults to 1 pre-n
  name: weight
  type: number
- description: Optional limit in hours after which the decay does not apply.
  name: limit_hours
  type: number
- description: Optional reference timestamp to calculate decay from.
  name: now
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-search-service-time-decay-schema.json
slug: cortex-search-service-time-decay
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: TimeDecay
---
