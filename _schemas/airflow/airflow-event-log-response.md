---
description: Event Log Response.
layout: schema
name: EventLogResponse
properties_list:
- description: ''
  name: event_log_id
  type: integer
- description: ''
  name: when
  type: string
- description: ''
  name: dag_id
  type: object
- description: ''
  name: task_id
  type: object
- description: ''
  name: run_id
  type: object
- description: ''
  name: map_index
  type: object
- description: ''
  name: try_number
  type: object
- description: ''
  name: event
  type: string
- description: ''
  name: logical_date
  type: object
- description: ''
  name: owner
  type: object
- description: ''
  name: extra
  type: object
- description: ''
  name: dag_display_name
  type: object
- description: ''
  name: task_display_name
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-event-log-response-schema.json
slug: airflow-event-log-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: EventLogResponse
---
