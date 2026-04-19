---
description: Request model for convert to managed iceberg table
layout: schema
name: ConvertToManagedIcebergTableRequest
properties_list:
- description: The path to a directory where Snowflake can write data and metadata files for the table.
  name: base_location
  type: string
- description: Specifies the storage serialization policy for the table.
  name: storage_serialization_policy
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-convert-to-managed-iceberg-table-request-schema.json
slug: iceberg-table-convert-to-managed-iceberg-table-request
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ConvertToManagedIcebergTableRequest
---
