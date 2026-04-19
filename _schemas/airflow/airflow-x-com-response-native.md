---
description: XCom response serializer with native return type.
layout: schema
name: XComResponseNative
properties_list:
- description: ''
  name: key
  type: string
- description: ''
  name: timestamp
  type: string
- description: ''
  name: logical_date
  type: object
- description: ''
  name: map_index
  type: integer
- description: ''
  name: task_id
  type: string
- description: ''
  name: dag_id
  type: string
- description: ''
  name: run_id
  type: string
- description: ''
  name: dag_display_name
  type: string
- description: ''
  name: task_display_name
  type: string
- description: ''
  name: run_after
  type: string
- description: ''
  name: value
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-x-com-response-native-schema.json
slug: airflow-x-com-response-native
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: XComResponseNative
---
