---
description: Object used for create backfill request.
layout: schema
name: BackfillPostBody
properties_list:
- description: ''
  name: dag_id
  type: string
- description: ''
  name: from_date
  type: string
- description: ''
  name: to_date
  type: string
- description: ''
  name: run_backwards
  type: boolean
- description: ''
  name: dag_run_conf
  type: object
- description: ''
  name: reprocess_behavior
  type: object
- description: ''
  name: max_active_runs
  type: integer
- description: ''
  name: run_on_latest_version
  type: boolean
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-backfill-post-body-schema.json
slug: airflow-backfill-post-body
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: BackfillPostBody
---
