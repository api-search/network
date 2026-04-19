---
description: SQL query request for the Aladdin Data Cloud
layout: schema
name: QueryRequest
properties_list:
- description: SQL query to execute against the Aladdin Data Cloud
  name: sql
  type: string
- description: Snowflake virtual warehouse to use
  name: warehouse
  type: string
- description: Query timeout in seconds
  name: timeout
  type: integer
- description: Maximum number of rows to return
  name: maxRows
  type: integer
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-data-cloud-query-request-schema.json
slug: aladdin-studio-data-cloud-query-request
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: QueryRequest
---
