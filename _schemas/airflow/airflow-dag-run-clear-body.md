---
description: DAG Run serializer for clear endpoint body.
layout: schema
name: DAGRunClearBody
properties_list:
- description: ''
  name: dry_run
  type: boolean
- description: ''
  name: only_failed
  type: boolean
- description: (Experimental) Run on the latest bundle version of the Dag after clearing the Dag Run.
  name: run_on_latest_version
  type: boolean
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-dag-run-clear-body-schema.json
slug: airflow-dag-run-clear-body
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: DAGRunClearBody
---
