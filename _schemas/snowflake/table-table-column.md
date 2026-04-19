---
description: A column in the table
layout: schema
name: TableColumn
properties_list:
- description: Column name
  name: name
  type: string
- description: The data type for the column
  name: datatype
  type: string
- description: Specifies that the column does allow NULL values or not.
  name: nullable
  type: boolean
- description: Specifies the collation to use for column operations such as string comparison
  name: collate
  type: string
- description: Specifies whether a default value is automatically inserted in the column if a value is not explicitly specified via an INSERT or CREATE TABLE AS SELECT statement
  name: default
  type: string
- description: ''
  name: autoincrement
  type: boolean
- description: The default value for the column starts with the specified number
  name: autoincrement_start
  type: integer
- description: Each successive value for the column automatically increments by the specified amount
  name: autoincrement_increment
  type: integer
- description: ''
  name: constraints
  type: array
- description: Specifies a comment for the column
  name: comment
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/table-table-column-schema.json
slug: table-table-column
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: TableColumn
---
