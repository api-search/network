---
description: ''
layout: schema
name: RunState
properties_list:
- description: Life cycle state of the run
  name: life_cycle_state
  type: string
- description: Result state of the run (available after completion)
  name: result_state
  type: string
- description: Descriptive message for the current state
  name: state_message
  type: string
- description: Whether the run was cancelled by a user or timed out
  name: user_cancelled_or_timedout
  type: boolean
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-run-state-schema.json
slug: azure-databricks-run-state
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: RunState
---
