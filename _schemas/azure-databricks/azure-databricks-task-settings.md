---
description: ''
layout: schema
name: TaskSettings
properties_list:
- description: Unique key for the task within the job. Must be unique among all tasks in the same job.
  name: task_key
  type: string
- description: Optional description for the task
  name: description
  type: string
- description: Tasks this task depends on. The task will not start until all dependent tasks complete successfully.
  name: depends_on
  type: array
- description: ID of an existing cluster to use for this task
  name: existing_cluster_id
  type: string
- description: Key of a job cluster specification to use. Refers to a cluster defined in the job's job_clusters field.
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
- description: Condition for running this task based on dependencies
  name: run_if
  type: string
- description: Timeout in seconds for this individual task
  name: timeout_seconds
  type: integer
- description: Maximum number of retries for this task
  name: max_retries
  type: integer
- description: Minimum interval between retries in milliseconds
  name: min_retry_interval_millis
  type: integer
- description: Whether to retry the task if it times out
  name: retry_on_timeout
  type: boolean
- description: Libraries to install on the task cluster
  name: libraries
  type: array
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-task-settings-schema.json
slug: azure-databricks-task-settings
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: TaskSettings
---
