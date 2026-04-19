---
consumed_apis:
- snowflake-sql
- snowflake-task
- snowflake-stream
- snowflake-pipe
- snowflake-stage
- snowflake-function
- snowflake-procedure
- snowflake-udf
- snowflake-result
description: Unified workflow for building and managing data pipelines using SQL execution, tasks, streams, pipes, stages, and functions. Used by Data Engineers to orchestrate ETL/ELT workflows and continuous data ingestion.
layout: capability
name: Snowflake Data Engineering
operations:
- description: Submit a SQL statement
  method: POST
  name: submit-statement
  path: /v1/statements
- description: List tasks
  method: GET
  name: list-tasks
  path: /v1/tasks
- description: Create a task
  method: POST
  name: create-task
  path: /v1/tasks
- description: List streams
  method: GET
  name: list-streams
  path: /v1/streams
- description: Create a stream
  method: POST
  name: create-stream
  path: /v1/streams
- description: List pipes
  method: GET
  name: list-pipes
  path: /v1/pipes
- description: Create a pipe
  method: POST
  name: create-pipe
  path: /v1/pipes
- description: List stages
  method: GET
  name: list-stages
  path: /v1/stages
- description: Create a stage
  method: POST
  name: create-stage
  path: /v1/stages
personas: []
provider_name: Snowflake
provider_slug: snowflake
search_terms:
- resume a suspended task
- data sharing
- data lakes
- get query result
- list stored procedures
- list procedures
- pipe management
- list user defined functions
- resume task
- execute task
- list change data capture streams
- sql statement execution
- cancel a running statement
- create a stored procedure
- execute a task immediately
- execute function
- submit a sql statement
- data warehousing
- list tasks
- list scheduled tasks
- list functions
- list streams
- submit sql
- execute a function
- create procedure
- create a function
- submit a sql statement for execution
- call a stored procedure
- call procedure
- create a pipe
- get a query result
- sql
- etl
- snowflake
- get status of a submitted statement
- get statement status
- stage management
- list stages
- create a scheduled task
- suspend task
- list data loading stages
- list stage files
- stream management
- create a stream
- create a stage
- create a cdc stream
- data pipelines
- create pipe
- create a pipe for continuous ingestion
- list udfs
- create stage
- create a task
- suspend a running task
- task management
- create function
- list data ingestion pipes
- refresh a pipe
- refresh pipe
- database
- list files in a stage
- data engineering
- create stream
- create task
- submit statement
- list pipes
- cancel statement
slug: data-engineering
tags:
- Snowflake
- Data Engineering
- ETL
- Data Pipelines
tools:
- description: Submit a SQL statement for execution
  hints:
    readOnly: false
  name: submit-sql
- description: Get status of a submitted statement
  hints:
    readOnly: true
  name: get-statement-status
- description: Cancel a running statement
  hints:
    destructive: true
  name: cancel-statement
- description: List scheduled tasks
  hints:
    readOnly: true
  name: list-tasks
- description: Create a scheduled task
  hints:
    readOnly: false
  name: create-task
- description: Execute a task immediately
  hints:
    readOnly: false
  name: execute-task
- description: Resume a suspended task
  hints:
    readOnly: false
  name: resume-task
- description: Suspend a running task
  hints:
    readOnly: false
  name: suspend-task
- description: List change data capture streams
  hints:
    readOnly: true
  name: list-streams
- description: Create a CDC stream
  hints:
    readOnly: false
  name: create-stream
- description: List data ingestion pipes
  hints:
    readOnly: true
  name: list-pipes
- description: Create a pipe for continuous ingestion
  hints:
    readOnly: false
  name: create-pipe
- description: Refresh a pipe
  hints:
    readOnly: false
  name: refresh-pipe
- description: List data loading stages
  hints:
    readOnly: true
  name: list-stages
- description: Create a stage
  hints:
    readOnly: false
  name: create-stage
- description: List files in a stage
  hints:
    readOnly: true
  name: list-stage-files
- description: List functions
  hints:
    readOnly: true
  name: list-functions
- description: Create a function
  hints:
    readOnly: false
  name: create-function
- description: Execute a function
  hints:
    readOnly: false
  name: execute-function
- description: List stored procedures
  hints:
    readOnly: true
  name: list-procedures
- description: Create a stored procedure
  hints:
    readOnly: false
  name: create-procedure
- description: Call a stored procedure
  hints:
    readOnly: false
  name: call-procedure
- description: List user defined functions
  hints:
    readOnly: true
  name: list-udfs
- description: Get a query result
  hints:
    readOnly: true
  name: get-query-result
---
