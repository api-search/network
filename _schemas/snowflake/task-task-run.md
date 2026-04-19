---
description: A task run executing a standalone task or a DAG of tasks starting from the root task.
layout: schema
name: TaskRun
properties_list:
- description: The name of the root task in the current task run.
  name: root_task_name
  type: string
- description: The name of the current database for the task run.
  name: database_name
  type: string
- description: The name of the current schema for the task run.
  name: schema_name
  type: string
- description: The current state of the task run.
  name: state
  type: string
- description: The name of the first task throwing an error in the task run.
  name: first_error_task_name
  type: string
- description: The first error code thrown in the task run.
  name: first_error_code
  type: integer
- description: The first error message thrown in the task run.
  name: first_error_message
  type: string
- description: The scheduled time for the task run.
  name: scheduled_time
  type: string
- description: The start time for the task run query.
  name: query_start_time
  type: string
- description: The next upcoming time for the task run.
  name: next_scheduled_time
  type: string
- description: The time this task run was last completed.
  name: completed_time
  type: string
- description: The unique task ID for the root task.
  name: root_task_id
  type: string
- description: The current version of the DAG on the task run.
  name: graph_version
  type: integer
- description: The unique ID for the current task run.
  name: run_id
  type: integer
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/task-task-run-schema.json
slug: task-task-run
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: TaskRun
---
