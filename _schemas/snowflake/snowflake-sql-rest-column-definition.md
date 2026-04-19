---
description: Describes a column in the result set.
layout: schema
name: ColumnDefinition
properties_list:
- description: Name of the column.
  name: name
  type: string
- description: Snowflake data type of the column (e.g. FIXED, TEXT, BOOLEAN, DATE, TIMESTAMP_NTZ, VARIANT, ARRAY, OBJECT).
  name: type
  type: string
- description: Maximum length of the column data.
  name: length
  type: integer
- description: Precision of numeric data.
  name: precision
  type: integer
- description: Scale of numeric data.
  name: scale
  type: integer
- description: Whether the column allows null values.
  name: nullable
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-column-definition-schema.json
slug: snowflake-sql-rest-column-definition
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ColumnDefinition
---
