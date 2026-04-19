---
description: Status returned when a query execution fails.
layout: schema
name: QueryFailureStatus
properties_list:
- description: Error code for the query failure.
  name: code
  type: string
- description: SQL state code indicating the error category.
  name: sqlState
  type: string
- description: Error message describing the failure.
  name: message
  type: string
- description: Handle that uniquely identifies the failed statement.
  name: statementHandle
  type: string
- description: Timestamp that specifies when the statement execution started. The timestamp is expressed in milliseconds since the epoch.
  name: createdOn
  type: integer
- description: URL for checking the status of the failed statement.
  name: statementStatusUrl
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-query-failure-status-schema.json
slug: snowflake-sql-rest-query-failure-status
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: QueryFailureStatus
---
