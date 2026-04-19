---
description: ''
layout: schema
name: JobEmailNotifications
properties_list:
- description: Email addresses to notify when a run starts.
  name: on_start
  type: array
- description: Email addresses to notify when a run succeeds.
  name: on_success
  type: array
- description: Email addresses to notify when a run fails.
  name: on_failure
  type: array
- description: ''
  name: on_duration_warning_threshold_exceeded
  type: array
- description: ''
  name: no_alert_for_skipped_runs
  type: boolean
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-job-email-notifications-schema.json
slug: databricks-job-email-notifications
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
title: JobEmailNotifications
---
