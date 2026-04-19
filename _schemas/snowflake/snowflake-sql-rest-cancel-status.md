---
description: Status returned when a statement cancellation is requested.
layout: schema
name: CancelStatus
properties_list:
- description: Status code for the cancellation.
  name: code
  type: string
- description: SQL state code.
  name: sqlState
  type: string
- description: Message describing the cancellation status.
  name: message
  type: string
- description: Handle of the canceled statement.
  name: statementHandle
  type: string
- description: URL for checking the status of the canceled statement.
  name: statementStatusUrl
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-cancel-status-schema.json
slug: snowflake-sql-rest-cancel-status
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: CancelStatus
---
