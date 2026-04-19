---
description: Metadata about the result set including column definitions.
layout: schema
name: ResultSetMetaData
properties_list:
- description: For v2 endpoints the only possible value for this field is jsonv2.
  name: format
  type: string
- description: The total number of rows of results.
  name: numRows
  type: integer
- description: Array of column descriptors for the result set.
  name: rowType
  type: array
- description: Information about result set partitions for large results.
  name: partitionInfo
  type: array
- description: If false, null values are replaced with the string 'null' in the result set.
  name: nullable
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-result-set-meta-data-schema.json
slug: snowflake-sql-rest-result-set-meta-data
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ResultSetMetaData
---
