---
description: Status of a query that is in progress or has completed successfully.
layout: schema
name: QueryStatus
properties_list:
- description: Status code for the query execution.
  name: code
  type: string
- description: SQL state code.
  name: sqlState
  type: string
- description: Message describing the status of the query.
  name: message
  type: string
- description: Handle that uniquely identifies the statement. You can use this handle to check the status of the statement and retrieve the result set.
  name: statementHandle
  type: string
- description: Timestamp that specifies when the statement execution started. The timestamp is expressed in milliseconds since the epoch.
  name: createdOn
  type: integer
- description: URL that you can use to check the status of the execution of the statement and retrieve the result set.
  name: statementStatusUrl
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-query-status-schema.json
slug: snowflake-sql-rest-query-status
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: QueryStatus
---
