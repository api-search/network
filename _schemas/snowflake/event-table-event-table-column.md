---
description: ''
layout: schema
name: EventTableColumn
properties_list:
- description: Column name
  name: name
  type: string
- description: The data type for the column
  name: datatype
  type: string
- description: Specifies that the column does allow NULL values or not
  name: nullable
  type: boolean
- description: Specifies whether a default value is automatically inserted in the column if a value is not explicitly specified via an INSERT or CREATE TABLE AS SELECT statement
  name: default
  type: string
- description: A primary key is the column or columns that contain values that uniquely identify each row in a table
  name: primary_key
  type: boolean
- description: Unique keys are columns in a table that uniquely identify items in the rows. This sounds a lot like a primary key, but the main difference is that unique keys can have NULL values.
  name: unique_key
  type: boolean
- description: ''
  name: check
  type: string
- description: ''
  name: expression
  type: string
- description: Specifies a comment for the column
  name: comment
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/event-table-event-table-column-schema.json
slug: event-table-event-table-column
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: EventTableColumn
---
