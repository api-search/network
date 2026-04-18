---
description: ''
layout: schema
name: EmailNotifications
properties_list:
- description: Email addresses to notify when a run starts
  name: on_start
  type: array
- description: Email addresses to notify when a run succeeds
  name: on_success
  type: array
- description: Email addresses to notify when a run fails
  name: on_failure
  type: array
- description: Email addresses to notify when a run exceeds the duration warning threshold
  name: on_duration_warning_threshold_exceeded
  type: array
- description: Do not send alert for skipped runs
  name: no_alert_for_skipped_runs
  type: boolean
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-email-notifications-schema.json
slug: azure-databricks-email-notifications
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: EmailNotifications
---
