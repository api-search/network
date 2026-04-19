---
description: Serializer for a xcom item.
layout: schema
name: XComResponse
properties_list:
- description: ''
  name: key
  type: string
- description: ''
  name: timestamp
  type: string
- description: ''
  name: logical_date
  type: object
- description: ''
  name: map_index
  type: integer
- description: ''
  name: task_id
  type: string
- description: ''
  name: dag_id
  type: string
- description: ''
  name: run_id
  type: string
- description: ''
  name: dag_display_name
  type: string
- description: ''
  name: task_display_name
  type: string
- description: ''
  name: run_after
  type: string
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-x-com-response-schema.json
slug: airflow-x-com-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: XComResponse
---
