---
description: Task serializer for responses.
layout: schema
name: TaskResponse
properties_list:
- description: ''
  name: task_id
  type: object
- description: ''
  name: task_display_name
  type: object
- description: ''
  name: owner
  type: object
- description: ''
  name: start_date
  type: object
- description: ''
  name: end_date
  type: object
- description: ''
  name: trigger_rule
  type: object
- description: ''
  name: depends_on_past
  type: boolean
- description: ''
  name: wait_for_downstream
  type: boolean
- description: ''
  name: retries
  type: object
- description: ''
  name: queue
  type: object
- description: ''
  name: pool
  type: object
- description: ''
  name: pool_slots
  type: object
- description: ''
  name: execution_timeout
  type: object
- description: ''
  name: retry_delay
  type: object
- description: ''
  name: retry_exponential_backoff
  type: number
- description: ''
  name: priority_weight
  type: object
- description: ''
  name: weight_rule
  type: object
- description: ''
  name: ui_color
  type: object
- description: ''
  name: ui_fgcolor
  type: object
- description: ''
  name: template_fields
  type: object
- description: ''
  name: downstream_task_ids
  type: object
- description: ''
  name: doc_md
  type: object
- description: ''
  name: operator_name
  type: object
- description: ''
  name: params
  type: object
- description: ''
  name: class_ref
  type: object
- description: ''
  name: is_mapped
  type: object
- description: Extract and return extra_links.
  name: extra_links
  type: array
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-task-response-schema.json
slug: airflow-task-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: TaskResponse
---
