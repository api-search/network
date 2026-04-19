---
description: Create table as select
layout: schema
name: TableAsSelect
properties_list:
- description: Specifies the name for the table, must be unique for the schema in which the table is created
  name: name
  type: string
- description: ''
  name: columns
  type: array
- description: Specifies one or more columns or column expressions in the table as the clustering key
  name: cluster_by
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/table-table-as-select-schema.json
slug: table-table-as-select
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: TableAsSelect
---
