---
description: Snowflake schema definition.
layout: schema
name: Schema
properties_list:
- description: Date and time the schema was created.
  name: created_on
  type: string
- description: Schema type, permanent (default) or transient.
  name: kind
  type: string
- description: Default schema for a user.
  name: is_default
  type: boolean
- description: Current schema for the session.
  name: is_current
  type: boolean
- description: Database that the schema belongs to
  name: database_name
  type: string
- description: Name of the role that owns the schema.
  name: owner
  type: string
- description: Optional comment in which to store information related to the schema.
  name: comment
  type: string
- description: ''
  name: options
  type: string
- description: Whether this schema is a managed access schema that centralizes privilege management with the schema owner.
  name: managed_access
  type: boolean
- description: Number of days that historical data is retained for Time Travel.
  name: retention_time
  type: integer
- description: Date and time the schema was dropped.
  name: dropped_on
  type: string
- description: Type of role that owns the object, either `ROLE` or `DATABASE_ROLE`.
  name: owner_role_type
  type: string
- description: Budget that defines a monthly spending limit on the compute costs for a Snowflake account or a custom group of Snowflake objects.
  name: budget
  type: string
- description: Number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, as well as specifying the default Time Travel retention time for all tables created in the schema
  name: data_retention_time_in_days
  type: integer
- description: Specifies a default collation specification for all tables added to the schema. You an override the default at the schema and individual table levels.
  name: default_ddl_collation
  type: string
- description: Severity level of messages that should be ingested and made available in the active event table. Currently, Snowflake supports only `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` and `OFF`.
  name: log_level
  type: string
- description: Whether pipe execution is paused.
  name: pipe_execution_paused
  type: boolean
- description: Maximum number of days for which Snowflake can extend the data retention period for tables in the schema to prevent streams on the tables from becoming stale.
  name: max_data_extension_time_in_days
  type: integer
- description: Specifies the number of consecutive failed task runs after which the current task is suspended automatically.
  name: suspend_task_after_num_failures
  type: integer
- description: How trace events are ingested into the event table. Currently, Snowflake supports only `ALWAYS`, `ON_EVENT`, and `OFF`.
  name: trace_level
  type: string
- description: Size of the compute resources to provision for the first run of the serverless task, before a task history is available for Snowflake to determine an ideal size.
  name: user_task_managed_initial_warehouse_size
  type: string
- description: Time limit, in milliseconds, for a single run of the task before it times out.
  name: user_task_timeout_ms
  type: integer
- description: Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.
  name: serverless_task_min_statement_size
  type: string
- description: Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE.
  name: serverless_task_max_statement_size
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/schema-schema-schema.json
slug: schema-schema
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Schema
---
