---
description: Request body for bulk update, and delete task instances.
layout: schema
name: BulkTaskInstanceBody
properties_list:
- description: ''
  name: new_state
  type: object
- description: ''
  name: note
  type: object
- description: ''
  name: include_upstream
  type: boolean
- description: ''
  name: include_downstream
  type: boolean
- description: ''
  name: include_future
  type: boolean
- description: ''
  name: include_past
  type: boolean
- description: ''
  name: task_id
  type: string
- description: ''
  name: map_index
  type: object
- description: ''
  name: dag_id
  type: object
- description: ''
  name: dag_run_id
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-bulk-task-instance-body-schema.json
slug: airflow-bulk-task-instance-body
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: BulkTaskInstanceBody
---
