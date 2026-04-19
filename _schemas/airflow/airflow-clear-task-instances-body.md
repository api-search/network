---
description: Request body for Clear Task Instances endpoint.
layout: schema
name: ClearTaskInstancesBody
properties_list:
- description: ''
  name: dry_run
  type: boolean
- description: ''
  name: start_date
  type: object
- description: ''
  name: end_date
  type: object
- description: ''
  name: only_failed
  type: boolean
- description: ''
  name: only_running
  type: boolean
- description: ''
  name: reset_dag_runs
  type: boolean
- description: A list of `task_id` or [`task_id`, `map_index`]. If only the `task_id` is provided for a mapped task, all of its map indices will be targeted.
  name: task_ids
  type: object
- description: ''
  name: dag_run_id
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
- description: (Experimental) Run on the latest bundle version of the dag after clearing the task instances.
  name: run_on_latest_version
  type: boolean
- description: ''
  name: prevent_running_task
  type: boolean
- description: ''
  name: note
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-clear-task-instances-body-schema.json
slug: airflow-clear-task-instances-body
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: ClearTaskInstancesBody
---
