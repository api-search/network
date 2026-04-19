---
description: Information about a partition of the result set.
layout: schema
name: PartitionInfo
properties_list:
- description: Number of rows in the partition.
  name: rowCount
  type: integer
- description: The partition size before decompression. This may not be present in every partition.
  name: compressedSize
  type: integer
- description: The partition size after decompression.
  name: uncompressedSize
  type: integer
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-partition-info-schema.json
slug: snowflake-sql-rest-partition-info
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: PartitionInfo
---
