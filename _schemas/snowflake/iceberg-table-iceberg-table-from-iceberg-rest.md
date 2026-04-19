---
description: Creates or replaces an Apache Iceberg™ table in the current/specified schema for an Iceberg REST catalog.
layout: schema
name: IcebergTableFromIcebergRest
properties_list:
- description: Specifies the name for the table, must be unique for the schema in which the table is created
  name: name
  type: string
- description: Specifies the name of the external volume to use for the table
  name: external_volume
  type: string
- description: Specifies the table name as recognized by the AWS Glue Data Catalog.
  name: catalog_table_name
  type: string
- description: Specifies the catalog namespace for the table.
  name: catalog_namespace
  type: string
- description: Specifies whether to replace invalid characters in the column names
  name: replace_invalid_characters
  type: boolean
- description: Specifies whether to automatically refresh the table metadata
  name: auto_refresh
  type: boolean
- description: Specifies the name of the catalog integration to use for the table
  name: catalog
  type: string
- description: Specifies a comment for the table
  name: comment
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-iceberg-table-from-iceberg-rest-schema.json
slug: iceberg-table-iceberg-table-from-iceberg-rest
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: IcebergTableFromIcebergRest
---
