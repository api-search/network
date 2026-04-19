---
description: Session parameters that should be set before executing the statement.
layout: schema
name: SessionParameters
properties_list:
- description: Time zone to use when executing the statement.
  name: timezone
  type: string
- description: Query tag that you want to associate with the SQL statement.
  name: query_tag
  type: string
- description: Output format for binary values.
  name: binary_output_format
  type: string
- description: Output format for DATE values.
  name: date_output_format
  type: string
- description: Output format for TIME values.
  name: time_output_format
  type: string
- description: Output format for TIMESTAMP values.
  name: timestamp_output_format
  type: string
- description: Output format for TIMESTAMP_LTZ values.
  name: timestamp_ltz_output_format
  type: string
- description: Output format for TIMESTAMP_NTZ values.
  name: timestamp_ntz_output_format
  type: string
- description: Output format for TIMESTAMP_TZ values.
  name: timestamp_tz_output_format
  type: string
- description: Number of statements to execute when using multi-statement capability. 0 implies variable number of statements. Negative numbers are not allowed.
  name: multi_statement_count
  type: integer
- description: Maximum size of each set (chunk) of query results to download.
  name: client_result_chunk_size
  type: integer
- description: Maximum number of rows returned in a result set.
  name: rows_per_resultset
  type: integer
- description: Whether to use a previously-cached result set for a query whose result set is still in the cache.
  name: use_cached_result
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-session-parameters-schema.json
slug: snowflake-sql-rest-session-parameters
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: SessionParameters
---
