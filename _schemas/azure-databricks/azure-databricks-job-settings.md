---
description: ''
layout: schema
name: JobSettings
properties_list:
- description: Optional name for the job. Default is Untitled.
  name: name
  type: string
- description: Map of tags associated with the job
  name: tags
  type: object
- description: List of task specifications for the job. A job must contain at least one task.
  name: tasks
  type: array
- description: A list of job cluster specifications that can be shared and reused by tasks.
  name: job_clusters
  type: array
- description: ''
  name: notification_settings
  type: object
- description: Timeout in seconds applied to each run of this job. Default is no timeout.
  name: timeout_seconds
  type: integer
- description: Maximum allowed number of concurrent runs of the job. Default is 1.
  name: max_concurrent_runs
  type: integer
- description: Trigger settings for file arrival events
  name: trigger
  type: object
- description: Settings for continuous job execution
  name: continuous
  type: object
- description: Format of the job. MULTI_TASK is the preferred format for creating jobs with multiple tasks.
  name: format
  type: string
- description: ''
  name: queue
  type: object
- description: Job-level parameters
  name: parameters
  type: array
- description: User or service principal to run the job as
  name: run_as
  type: object
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-job-settings-schema.json
slug: azure-databricks-job-settings
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: JobSettings
---
