---
description: A column in the snowflake catalog iceberg table
layout: schema
name: IcebergTableColumn
properties_list:
- description: Column name
  name: name
  type: string
- description: The data type for the column
  name: datatype
  type: string
- description: Specifies a comment for the column
  name: comment
  type: string
- description: Argument null return acceptance criteria
  name: nullable
  type: boolean
- description: Default value for the column
  name: default_value
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-iceberg-table-column-schema.json
slug: iceberg-table-iceberg-table-column
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: IcebergTableColumn
---
