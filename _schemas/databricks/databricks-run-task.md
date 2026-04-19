---
description: ''
layout: schema
name: RunTask
properties_list:
- description: ''
  name: run_id
  type: integer
- description: ''
  name: task_key
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: state
  type: object
- description: ''
  name: depends_on
  type: array
- description: ''
  name: existing_cluster_id
  type: string
- description: ''
  name: notebook_task
  type: object
- description: ''
  name: spark_jar_task
  type: object
- description: ''
  name: spark_python_task
  type: object
- description: ''
  name: sql_task
  type: object
- description: ''
  name: start_time
  type: integer
- description: ''
  name: setup_duration
  type: integer
- description: ''
  name: execution_duration
  type: integer
- description: ''
  name: cleanup_duration
  type: integer
- description: ''
  name: end_time
  type: integer
- description: ''
  name: cluster_instance
  type: object
- description: ''
  name: attempt_number
  type: integer
- description: ''
  name: libraries
  type: array
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-run-task-schema.json
slug: databricks-run-task
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
title: RunTask
---
