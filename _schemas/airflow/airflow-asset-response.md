---
description: Asset serializer for responses.
layout: schema
name: AssetResponse
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: name
  type: string
- description: ''
  name: uri
  type: string
- description: ''
  name: group
  type: string
- description: ''
  name: extra
  type: object
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: scheduled_dags
  type: array
- description: ''
  name: producing_tasks
  type: array
- description: ''
  name: consuming_tasks
  type: array
- description: ''
  name: aliases
  type: array
- description: ''
  name: watchers
  type: array
- description: ''
  name: last_asset_event
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-asset-response-schema.json
slug: airflow-asset-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: AssetResponse
---
