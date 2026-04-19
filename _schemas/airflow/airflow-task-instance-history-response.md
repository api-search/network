---
description: TaskInstanceHistory serializer for responses.
layout: schema
name: TaskInstanceHistoryResponse
properties_list:
- description: ''
  name: task_id
  type: string
- description: ''
  name: dag_id
  type: string
- description: ''
  name: dag_run_id
  type: string
- description: ''
  name: map_index
  type: integer
- description: ''
  name: start_date
  type: object
- description: ''
  name: end_date
  type: object
- description: ''
  name: duration
  type: object
- description: ''
  name: state
  type: object
- description: ''
  name: try_number
  type: integer
- description: ''
  name: max_tries
  type: integer
- description: ''
  name: task_display_name
  type: string
- description: ''
  name: dag_display_name
  type: string
- description: ''
  name: hostname
  type: object
- description: ''
  name: unixname
  type: object
- description: ''
  name: pool
  type: string
- description: ''
  name: pool_slots
  type: integer
- description: ''
  name: queue
  type: object
- description: ''
  name: priority_weight
  type: object
- description: ''
  name: operator
  type: object
- description: ''
  name: operator_name
  type: object
- description: ''
  name: queued_when
  type: object
- description: ''
  name: scheduled_when
  type: object
- description: ''
  name: pid
  type: object
- description: ''
  name: executor
  type: object
- description: ''
  name: executor_config
  type: string
- description: ''
  name: dag_version
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-task-instance-history-response-schema.json
slug: airflow-task-instance-history-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: TaskInstanceHistoryResponse
---
