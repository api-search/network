---
description: Pool serializer for post bodies.
layout: schema
name: PoolBody
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
  name: team_name
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-pool-body-schema.json
slug: airflow-pool-body
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: PoolBody
---
