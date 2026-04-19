---
description: ''
layout: schema
name: StreamSource
properties_list:
- description: 'Type of the source. Possible values include: stream, table, view'
  name: src_type
  type: string
- description: Name of the source whose changes are tracked by the stream
  name: name
  type: string
- description: Database name to which stream source type belongs. If not provided, database name provided in the path param will be used.
  name: database_name
  type: string
- description: Schema name to which stream source type belongs. If not provided, schema name provided in the path param will be used.
  name: schema_name
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/stream-stream-source-schema.json
slug: stream-stream-source
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: StreamSource
---
