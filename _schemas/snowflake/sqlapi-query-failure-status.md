---
description: ''
layout: schema
name: QueryFailureStatus
properties_list:
- description: ''
  name: code
  type: string
- description: ''
  name: sqlState
  type: string
- description: ''
  name: message
  type: string
- description: ''
  name: statementHandle
  type: string
- description: Timestamp that specifies when the statement execution started.‌ The timestamp is expressed in milliseconds since the epoch.
  name: createdOn
  type: integer
- description: ''
  name: statementStatusUrl
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/sqlapi-query-failure-status-schema.json
slug: sqlapi-query-failure-status
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: QueryFailureStatus
---
