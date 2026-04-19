---
description: Create iceberg table from Iceberg files
layout: schema
name: IcebergTableFromIcebergFiles
properties_list:
- description: Specifies the name for the table, must be unique for the schema in which the table is created
  name: name
  type: string
- description: Specifies the name of the external volume to use for the table
  name: external_volume
  type: string
- description: Specifies whether to replace invalid characters in the column names
  name: replace_invalid_characters
  type: boolean
- description: Specifies the relative path of the Iceberg metadata file to use for column definitions.
  name: metadata_file_path
  type: string
- description: Specifies the name of the catalog integration to use for the table
  name: catalog
  type: string
- description: Specifies a comment for the table
  name: comment
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-iceberg-table-from-iceberg-files-schema.json
slug: iceberg-table-iceberg-table-from-iceberg-files
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: IcebergTableFromIcebergFiles
---
