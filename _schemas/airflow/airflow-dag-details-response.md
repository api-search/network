---
description: Specific serializer for DAG Details responses.
layout: schema
name: DAGDetailsResponse
properties_list:
- description: ''
  name: dag_id
  type: string
- description: ''
  name: dag_display_name
  type: string
- description: ''
  name: is_paused
  type: boolean
- description: ''
  name: is_stale
  type: boolean
- description: ''
  name: last_parsed_time
  type: object
- description: ''
  name: last_parse_duration
  type: object
- description: ''
  name: last_expired
  type: object
- description: ''
  name: bundle_name
  type: object
- description: ''
  name: bundle_version
  type: object
- description: ''
  name: relative_fileloc
  type: object
- description: ''
  name: fileloc
  type: string
- description: ''
  name: description
  type: object
- description: ''
  name: timetable_summary
  type: object
- description: ''
  name: timetable_description
  type: object
- description: ''
  name: timetable_partitioned
  type: boolean
- description: ''
  name: timetable_periodic
  type: boolean
- description: ''
  name: tags
  type: array
- description: ''
  name: max_active_tasks
  type: integer
- description: ''
  name: max_active_runs
  type: object
- description: ''
  name: max_consecutive_failed_dag_runs
  type: integer
- description: ''
  name: has_task_concurrency_limits
  type: boolean
- description: ''
  name: has_import_errors
  type: boolean
- description: ''
  name: next_dagrun_logical_date
  type: object
- description: ''
  name: next_dagrun_data_interval_start
  type: object
- description: ''
  name: next_dagrun_data_interval_end
  type: object
- description: ''
  name: next_dagrun_run_after
  type: object
- description: ''
  name: allowed_run_types
  type: object
- description: ''
  name: owners
  type: array
- description: ''
  name: catchup
  type: boolean
- description: ''
  name: dag_run_timeout
  type: object
- description: ''
  name: asset_expression
  type: object
- description: ''
  name: doc_md
  type: object
- description: ''
  name: start_date
  type: object
- description: ''
  name: end_date
  type: object
- description: ''
  name: is_paused_upon_creation
  type: object
- description: ''
  name: params
  type: object
- description: ''
  name: render_template_as_native_obj
  type: boolean
- description: ''
  name: template_search_path
  type: object
- description: ''
  name: timezone
  type: object
- description: ''
  name: last_parsed
  type: object
- description: ''
  name: default_args
  type: object
- description: ''
  name: owner_links
  type: object
- description: ''
  name: is_favorite
  type: boolean
- description: ''
  name: active_runs_count
  type: integer
- description: Whether this DAG's schedule supports backfilling.
  name: is_backfillable
  type: boolean
- description: Return file token.
  name: file_token
  type: string
- description: 'Return max_active_tasks as concurrency. Deprecated: Use max_active_tasks instead.'
  name: concurrency
  type: integer
- description: Return the latest DagVersion.
  name: latest_dag_version
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-dag-details-response-schema.json
slug: airflow-dag-details-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: DAGDetailsResponse
---
