---
description: The result set returned from a successfully executed SQL statement, including metadata, row data, and execution statistics.
layout: schema
name: ResultSet
properties_list:
- description: Status code for the query.
  name: code
  type: string
- description: SQL state code.
  name: sqlState
  type: string
- description: Message describing the execution status.
  name: message
  type: string
- description: Handle that uniquely identifies the executed statement.
  name: statementHandle
  type: string
- description: Timestamp that specifies when the statement execution started. The timestamp is expressed in milliseconds since the epoch.
  name: createdOn
  type: integer
- description: URL for checking the status of the statement.
  name: statementStatusUrl
  type: string
- description: Result set data. Each element in the outer array represents a row. Each element in the inner array represents a column value as a string.
  name: data
  type: array
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-result-set-schema.json
slug: snowflake-sql-rest-result-set
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ResultSet
---
