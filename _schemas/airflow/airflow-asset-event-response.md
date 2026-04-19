---
description: Asset event serializer for responses.
layout: schema
name: AssetEventResponse
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: asset_id
  type: integer
- description: ''
  name: uri
  type: object
- description: ''
  name: name
  type: object
- description: ''
  name: group
  type: object
- description: ''
  name: extra
  type: object
- description: ''
  name: source_task_id
  type: object
- description: ''
  name: source_dag_id
  type: object
- description: ''
  name: source_run_id
  type: object
- description: ''
  name: source_map_index
  type: integer
- description: ''
  name: created_dagruns
  type: array
- description: ''
  name: timestamp
  type: string
- description: ''
  name: partition_key
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-asset-event-response-schema.json
slug: airflow-asset-event-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: AssetEventResponse
---
