---
description: Schema for Human-in-the-loop detail history.
layout: schema
name: HITLDetailHistory
properties_list:
- description: ''
  name: options
  type: array
- description: ''
  name: subject
  type: string
- description: ''
  name: body
  type: object
- description: ''
  name: defaults
  type: object
- description: ''
  name: multiple
  type: boolean
- description: ''
  name: params
  type: object
- description: ''
  name: assigned_users
  type: array
- description: ''
  name: created_at
  type: string
- description: ''
  name: responded_by_user
  type: object
- description: ''
  name: responded_at
  type: object
- description: ''
  name: chosen_options
  type: object
- description: ''
  name: params_input
  type: object
- description: ''
  name: response_received
  type: boolean
- description: ''
  name: task_instance
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-hitl-detail-history-schema.json
slug: airflow-hitl-detail-history
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: HITLDetailHistory
---
