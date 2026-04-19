---
description: Request model for refreshing iceberg table
layout: schema
name: RefreshIcebergTableRequest
properties_list:
- description: Specifies a metadata file path for a table created from Iceberg files in object storage.
  name: metadata_file_relative_path
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/iceberg-table-refresh-iceberg-table-request-schema.json
slug: iceberg-table-refresh-iceberg-table-request
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: RefreshIcebergTableRequest
---
