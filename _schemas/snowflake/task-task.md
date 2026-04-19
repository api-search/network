---
description: A Snowflake task, used to execute SQL code.
layout: schema
name: Task
properties_list:
- description: Specifies a comment for the task.
  name: comment
  type: string
- description: Specifies the name of the root task that the finalizer task is associated with.
  name: finalize
  type: string
- description: Root task settable only. Specifies the number of automatic task graph retry attempts. Valid range is 0 to 30. When not specified, no retry would happen.
  name: task_auto_retry_attempts
  type: integer
- description: Task Config
  name: config
  type: object
- description: Session Parameters for the task at runtime.
  name: session_parameters
  type: object
- description: The SQL definition for the task. Any one of single SQL statement, call to stored procedure, or procedural logic using Snowflake scripting.
  name: definition
  type: string
- description: Specifies one or more predecessor tasks for the current task
  name: predecessors
  type: array
- description: Displays the relationship between the root task and its corresponding finalizer tasks.
  name: task_relations
  type: string
- description: Specifies the size of the compute resources to provision for the first run of the task. This parameter only applies to serverless tasks.
  name: user_task_managed_initial_warehouse_size
  type: string
- description: Specifies the minimum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.
  name: serverless_task_min_statement_size
  type: string
- description: Specifies the maximum allowed warehouse size for the serverless task. Minimum XSMALL, Maximum XXLARGE. This parameter only applies to serverless tasks.
  name: serverless_task_max_statement_size
  type: string
- description: Specifies the time limit on a single run of the task before it times out (in milliseconds).
  name: user_task_timeout_ms
  type: integer
- description: Specifies the number of consecutive failed task runs after which the current task is suspended automatically.
  name: suspend_task_after_num_failures
  type: integer
- description: Specifies a Boolean SQL expression condition; multiple conditions joined with AND/OR are supported
  name: condition
  type: string
- description: Specifies whether to allow multiple instances of the DAG to run concurrently.
  name: allow_overlapping_execution
  type: boolean
- description: Specifies the name of the notification integration used to communicate with Amazon SNS, MS Azure Event Grid, or Google Pub/Sub.
  name: error_integration
  type: string
- description: The time the task was created on.
  name: created_on
  type: string
- description: An ID for the current task.
  name: id
  type: string
- description: The role that owns the task.
  name: owner
  type: string
- description: The role type of the task owner.
  name: owner_role_type
  type: string
- description: The state of the task. Must be one of started or suspended.
  name: state
  type: string
- description: The time the task was last committed on.
  name: last_committed_on
  type: string
- description: The time the task was last suspended on.
  name: last_suspended_on
  type: string
- description: The name of the parent database for the task.
  name: database_name
  type: string
- description: The name of the parent schema for the task.
  name: schema_name
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/task-task-schema.json
slug: task-task
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: Task
---
