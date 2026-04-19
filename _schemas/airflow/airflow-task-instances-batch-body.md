---
description: Task Instance body for get batch.
layout: schema
name: TaskInstancesBatchBody
properties_list:
- description: ''
  name: dag_ids
  type: object
- description: ''
  name: dag_run_ids
  type: object
- description: ''
  name: task_ids
  type: object
- description: ''
  name: state
  type: object
- description: ''
  name: run_after_gte
  type: object
- description: ''
  name: run_after_gt
  type: object
- description: ''
  name: run_after_lte
  type: object
- description: ''
  name: run_after_lt
  type: object
- description: ''
  name: logical_date_gte
  type: object
- description: ''
  name: logical_date_gt
  type: object
- description: ''
  name: logical_date_lte
  type: object
- description: ''
  name: logical_date_lt
  type: object
- description: ''
  name: start_date_gte
  type: object
- description: ''
  name: start_date_gt
  type: object
- description: ''
  name: start_date_lte
  type: object
- description: ''
  name: start_date_lt
  type: object
- description: ''
  name: end_date_gte
  type: object
- description: ''
  name: end_date_gt
  type: object
- description: ''
  name: end_date_lte
  type: object
- description: ''
  name: end_date_lt
  type: object
- description: ''
  name: duration_gte
  type: object
- description: ''
  name: duration_gt
  type: object
- description: ''
  name: duration_lte
  type: object
- description: ''
  name: duration_lt
  type: object
- description: ''
  name: pool
  type: object
- description: ''
  name: queue
  type: object
- description: ''
  name: executor
  type: object
- description: ''
  name: page_offset
  type: integer
- description: ''
  name: page_limit
  type: integer
- description: ''
  name: order_by
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-task-instances-batch-body-schema.json
slug: airflow-task-instances-batch-body
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: TaskInstancesBatchBody
---
