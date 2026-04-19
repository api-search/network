---
description: ''
layout: schema
name: StreamSourceView
properties_list:
- description: Whether this stream is an append only stream or not
  name: append_only
  type: boolean
- description: Whether this stream show initial rows on first consumption
  name: show_initial_rows
  type: boolean
- description: List of base tables for the stream
  name: base_tables
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/stream-stream-source-view-schema.json
slug: stream-stream-source-view
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: StreamSourceView
---
