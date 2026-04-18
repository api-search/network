---
description: ''
layout: schema
name: CronSchedule
properties_list:
- description: Quartz cron expression for the schedule. See http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html
  name: quartz_cron_expression
  type: string
- description: Java timezone ID for the schedule
  name: timezone_id
  type: string
- description: Whether the schedule is paused or active
  name: pause_status
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-cron-schedule-schema.json
slug: azure-databricks-cron-schedule
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: CronSchedule
---
