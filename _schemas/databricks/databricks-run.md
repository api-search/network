---
description: ''
layout: schema
name: Run
properties_list:
- description: ''
  name: job_id
  type: integer
- description: The canonical identifier of the run.
  name: run_id
  type: integer
- description: ''
  name: run_name
  type: string
- description: ''
  name: number_in_job
  type: integer
- description: ''
  name: original_attempt_run_id
  type: integer
- description: ''
  name: state
  type: object
- description: ''
  name: tasks
  type: array
- description: ''
  name: job_clusters
  type: array
- description: ''
  name: cluster_spec
  type: object
- description: ''
  name: cluster_instance
  type: object
- description: The start time of the run in epoch milliseconds.
  name: start_time
  type: integer
- description: Setup duration in milliseconds.
  name: setup_duration
  type: integer
- description: Execution duration in milliseconds.
  name: execution_duration
  type: integer
- description: Cleanup duration in milliseconds.
  name: cleanup_duration
  type: integer
- description: End time in epoch milliseconds.
  name: end_time
  type: integer
- description: ''
  name: trigger
  type: string
- description: ''
  name: run_type
  type: string
- description: ''
  name: attempt_number
  type: integer
- description: ''
  name: creator_user_name
  type: string
- description: URL of the run page in the Databricks workspace.
  name: run_page_url
  type: string
- description: ''
  name: format
  type: string
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-run-schema.json
slug: databricks-run
tags:
- AI
- Analytics
- Apache Spark
- Big Data
- Clean Rooms
- Cloud Computing
- Data
- Data Analytics
- Data Engineering
- Data Governance
- Delta Lake
- Delta Sharing
- ETL
- Identity Management
- Lakehouse
- Machine Learning
- MLflow
- Model Serving
- Security
- SQL
- Unity Catalog
- Vector Search
- Visualize
title: Run
---
