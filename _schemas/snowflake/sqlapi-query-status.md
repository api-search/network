---
description: ''
layout: schema
name: QueryStatus
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
- description: Timestamp that specifies when the statement execution started. The timestamp is expressed in milliseconds since the epoch.
  name: createdOn
  type: integer
- description: URL that you can use to check the status of the execution of the statement and the result set.
  name: statementStatusUrl
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/sqlapi-query-status-schema.json
slug: sqlapi-query-status
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: QueryStatus
---
