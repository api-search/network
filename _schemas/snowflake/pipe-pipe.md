---
description: A Snowflake pipe
layout: schema
name: Pipe
properties_list:
- description: Name of the pipe
  name: name
  type: string
- description: user comment associated to an object in the dictionary
  name: comment
  type: string
- description: TRUE if all files from stage need to be auto-ingested
  name: auto_ingest
  type: boolean
- description: Link to integration object that point to a user provided Azure storage queue / SQS. When present, errors (e.g. ingest failure for Snowpipe or a user task failure or replication failure) will be sent t
  name: error_integration
  type: string
- description: Optional, if provided, auto_ingest pipe will only receive messages from this SNS topic.
  name: aws_sns_topic
  type: string
- description: Link to integration object that ties a user provided storage queue to an auto_ingest enabled pipe. Required for auto_ingest to work on azure.
  name: integration
  type: string
- description: COPY INTO <table> statement used to load data from queued files into a Snowflake table. This statement serves as the text/definition for the pipe and is displayed in the SHOW PIPES output
  name: copy_statement
  type: string
- description: Date and time when the pipe was created.
  name: created_on
  type: string
- description: Database in which the pipe is stored
  name: database_name
  type: string
- description: Schema in which the pipe is stored
  name: schema_name
  type: string
- description: Role that owns the pipe
  name: owner
  type: string
- description: PATTERN copy option value in the COPY INTO <table> statement in the pipe definition, if the copy option was specified.
  name: pattern
  type: string
- description: The type of role that owns the pipe
  name: owner_role_type
  type: string
- description: Displays some detailed information for your pipes that may have issues
  name: invalid_reason
  type: string
- description: Name of the budget if the pipe is monitored by a budget
  name: budget
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/pipe-pipe-schema.json
slug: pipe-pipe
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Pipe
---
