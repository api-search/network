---
description: Pool serializer for responses.
layout: schema
name: PoolResponse
properties_list:
- description: ''
  name: name
  type: string
- description: Number of slots. Use -1 for unlimited.
  name: slots
  type: integer
- description: ''
  name: description
  type: object
- description: ''
  name: include_deferred
  type: boolean
- description: ''
  name: occupied_slots
  type: integer
- description: ''
  name: running_slots
  type: integer
- description: ''
  name: queued_slots
  type: integer
- description: ''
  name: scheduled_slots
  type: integer
- description: ''
  name: open_slots
  type: integer
- description: ''
  name: deferred_slots
  type: integer
- description: ''
  name: team_name
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-pool-response-schema.json
slug: airflow-pool-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: PoolResponse
---
