---
description: DAG Run serializer for responses.
layout: schema
name: DAGRunResponse
properties_list:
- description: ''
  name: dag_run_id
  type: string
- description: ''
  name: dag_id
  type: string
- description: ''
  name: logical_date
  type: object
- description: ''
  name: queued_at
  type: object
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
  name: data_interval_start
  type: object
- description: ''
  name: data_interval_end
  type: object
- description: ''
  name: run_after
  type: string
- description: ''
  name: last_scheduling_decision
  type: object
- description: ''
  name: run_type
  type: object
- description: ''
  name: state
  type: object
- description: ''
  name: triggered_by
  type: object
- description: ''
  name: triggering_user_name
  type: object
- description: ''
  name: conf
  type: object
- description: ''
  name: note
  type: object
- description: ''
  name: dag_versions
  type: array
- description: ''
  name: bundle_version
  type: object
- description: ''
  name: dag_display_name
  type: string
- description: ''
  name: partition_key
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-dag-run-response-schema.json
slug: airflow-dag-run-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: DAGRunResponse
---
