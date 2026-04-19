---
description: ''
layout: schema
name: Job
properties_list:
- description: The canonical identifier for this job.
  name: job_id
  type: integer
- description: The email of the user who created the job.
  name: creator_user_name
  type: string
- description: The email of the user the job runs as.
  name: run_as_user_name
  type: string
- description: The time the job was created in epoch milliseconds.
  name: created_time
  type: integer
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-job-schema.json
slug: databricks-job
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
title: Job
---
