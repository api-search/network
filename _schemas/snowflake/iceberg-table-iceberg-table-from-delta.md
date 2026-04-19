---
description: Create iceberg table from Delta
layout: schema
name: IcebergTableFromDelta
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
- description: Specifies a relative path from the table’s EXTERNAL_VOLUME location to a directory where Snowflake can access your Delta table files.
  name: base_location
  type: string
- description: Specifies the name of the catalog integration to use for the table
  name: catalog
  type: string
- description: Specifies a comment for the table
  name: comment
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-iceberg-table-from-delta-schema.json
slug: iceberg-table-iceberg-table-from-delta
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: IcebergTableFromDelta
---
