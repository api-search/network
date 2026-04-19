---
description: ''
layout: schema
name: CronSchedule
properties_list:
- description: A Quartz cron expression describing the schedule. See http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html
  name: quartz_cron_expression
  type: string
- description: A Java timezone ID. The schedule is resolved relative to this timezone.
  name: timezone_id
  type: string
- description: Whether the schedule is paused.
  name: pause_status
  type: string
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-cron-schedule-schema.json
slug: databricks-cron-schedule
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
title: CronSchedule
---
