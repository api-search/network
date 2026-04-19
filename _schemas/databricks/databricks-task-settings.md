---
description: ''
layout: schema
name: TaskSettings
properties_list:
- description: A unique key for the task within the job. Used to reference the task in dependencies and logging.
  name: task_key
  type: string
- description: A description of the task.
  name: description
  type: string
- description: An array of objects specifying the task dependencies. Each dependency is identified by its task_key.
  name: depends_on
  type: array
- description: An existing cluster to run the task on.
  name: existing_cluster_id
  type: string
- description: Reference to a job_clusters entry.
  name: job_cluster_key
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
  name: spark_submit_task
  type: object
- description: ''
  name: pipeline_task
  type: object
- description: ''
  name: python_wheel_task
  type: object
- description: ''
  name: sql_task
  type: object
- description: ''
  name: dbt_task
  type: object
- description: Condition to run this task.
  name: run_if
  type: string
- description: Timeout for this individual task.
  name: timeout_seconds
  type: integer
- description: Maximum number of retries for a failed task.
  name: max_retries
  type: integer
- description: Minimum interval between retry attempts.
  name: min_retry_interval_millis
  type: integer
- description: Whether to retry when the task times out.
  name: retry_on_timeout
  type: boolean
- description: Libraries to install on the cluster running this task.
  name: libraries
  type: array
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-task-settings-schema.json
slug: databricks-task-settings
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
title: TaskSettings
---
