---
description: Base serializer for Backfill.
layout: schema
name: BackfillResponse
properties_list:
- description: ''
  name: id
  type: integer
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
  name: dag_run_conf
  type: object
- description: ''
  name: is_paused
  type: boolean
- description: ''
  name: reprocess_behavior
  type: object
- description: ''
  name: max_active_runs
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: completed_at
  type: object
- description: ''
  name: updated_at
  type: string
- description: ''
  name: dag_display_name
  type: string
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-backfill-response-schema.json
slug: airflow-backfill-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: BackfillResponse
---
