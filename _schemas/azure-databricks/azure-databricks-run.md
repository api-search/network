---
description: ''
layout: schema
name: Run
properties_list:
- description: Canonical identifier of the run
  name: run_id
  type: integer
- description: ID of the job this run belongs to
  name: job_id
  type: integer
- description: Name of the run
  name: run_name
  type: string
- description: Username of the user who triggered the run
  name: creator_user_name
  type: string
- description: Sequence number of this run among all runs of the job
  name: number_in_job
  type: integer
- description: ''
  name: tasks
  type: array
- description: ''
  name: cluster_spec
  type: object
- description: ''
  name: cluster_instance
  type: object
- description: Start time of the run (epoch milliseconds)
  name: start_time
  type: integer
- description: Time spent setting up the cluster in milliseconds
  name: setup_duration
  type: integer
- description: Time spent executing the run in milliseconds
  name: execution_duration
  type: integer
- description: Time spent cleaning up after the run in milliseconds
  name: cleanup_duration
  type: integer
- description: End time of the run (epoch milliseconds)
  name: end_time
  type: integer
- description: What triggered this run
  name: trigger
  type: string
- description: ''
  name: run_type
  type: string
- description: Current attempt number of the run
  name: attempt_number
  type: integer
- description: URL of the run page in the Databricks UI
  name: run_page_url
  type: string
- description: ''
  name: format
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-run-schema.json
slug: azure-databricks-run
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: Run
---
