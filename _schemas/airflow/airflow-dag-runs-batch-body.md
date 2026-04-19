---
description: List DAG Runs body for batch endpoint.
layout: schema
name: DAGRunsBatchBody
properties_list:
- description: ''
  name: order_by
  type: object
- description: ''
  name: page_offset
  type: integer
- description: ''
  name: page_limit
  type: integer
- description: ''
  name: dag_ids
  type: object
- description: ''
  name: states
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
  name: conf_contains
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-dag-runs-batch-body-schema.json
slug: airflow-dag-runs-batch-body
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: DAGRunsBatchBody
---
