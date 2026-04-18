---
description: ''
layout: schema
name: Job
properties_list:
- description: Canonical identifier of the job
  name: job_id
  type: integer
- description: Username of the job creator
  name: creator_user_name
  type: string
- description: User the job runs as
  name: run_as_user_name
  type: string
- description: Time the job was created (epoch milliseconds)
  name: created_time
  type: integer
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-job-schema.json
slug: azure-databricks-job
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: Job
---
