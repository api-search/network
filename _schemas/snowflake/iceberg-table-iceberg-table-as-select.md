---
description: Create iceberg table as select
layout: schema
name: IcebergTableAsSelect
properties_list:
- description: Specifies the name for the table, must be unique for the schema in which the table is created
  name: name
  type: string
- description: ''
  name: columns
  type: array
- description: Specifies the name of the external volume to use for the table
  name: external_volume
  type: string
- description: Specifies one or more columns or column expressions in the table as the clustering key
  name: cluster_by
  type: array
- description: Specifies the path to a directory where Snowflake can write data and metadata files for the table
  name: base_location
  type: string
- description: Specifies a comment for the table
  name: comment
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-iceberg-table-as-select-schema.json
slug: iceberg-table-iceberg-table-as-select
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: IcebergTableAsSelect
---
