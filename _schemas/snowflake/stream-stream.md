---
description: A Snowflake stream
layout: schema
name: Stream
properties_list:
- description: Date and time when the stream was created.
  name: created_on
  type: string
- description: Name of the stream
  name: name
  type: string
- description: user comment associated to an object in the dictionary
  name: comment
  type: string
- description: Database in which the stream is stored
  name: database_name
  type: string
- description: Schema in which the stream is stored
  name: schema_name
  type: string
- description: Role that owns the stream
  name: owner
  type: string
- description: Table name whose changes are tracked by the stream
  name: table_name
  type: string
- description: Specifies whether the stream is stale or not
  name: stale
  type: boolean
- description: 'Mode of the stream. Possible values include: APPEND_ONLY, INSERT_ONLY. For streams on tables, the column displays DEFAULT.'
  name: mode
  type: string
- description: Timestamp when the stream became stale or may become stale if not consumed.
  name: stale_after
  type: string
- description: Reason why the stream cannot be queried successfully. This column supports future functionality. Currently, the only value returned is N/A.
  name: invalid_reason
  type: string
- description: The type of role that owns the stream
  name: owner_role_type
  type: string
- description: Type of the stream; currently DELTA only.
  name: type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/stream-stream-schema.json
slug: stream-stream
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Stream
---
