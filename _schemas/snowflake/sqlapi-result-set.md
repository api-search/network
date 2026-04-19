---
description: ''
layout: schema
name: ResultSet
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
- description: Timestamp that specifies when the statement execution started.‌ The timestamp is expressed in milliseconds since the epoch.‌
  name: createdOn
  type: integer
- description: ''
  name: statementStatusUrl
  type: string
- description: ''
  name: resultSetMetaData
  type: object
- description: Result set data.
  name: data
  type: array
- description: these stats might not be available for each request.
  name: stats
  type: object
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/sqlapi-result-set-schema.json
slug: sqlapi-result-set
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ResultSet
---
