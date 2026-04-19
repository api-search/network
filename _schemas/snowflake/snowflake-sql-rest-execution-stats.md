---
description: Statistics about the execution of the statement. These stats might not be available for each request.
layout: schema
name: ExecutionStats
properties_list:
- description: Number of rows that were inserted.
  name: numRowsInserted
  type: integer
- description: Number of rows that were updated.
  name: numRowsUpdated
  type: integer
- description: Number of rows that were deleted.
  name: numRowsDeleted
  type: integer
- description: Number of duplicate rows that were updated.
  name: numDuplicateRowsUpdated
  type: integer
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/snowflake-sql-rest-execution-stats-schema.json
slug: snowflake-sql-rest-execution-stats
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ExecutionStats
---
