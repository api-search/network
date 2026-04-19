---
description: Job serializer for responses.
layout: schema
name: JobResponse
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: dag_id
  type: object
- description: ''
  name: state
  type: object
- description: ''
  name: job_type
  type: object
- description: ''
  name: start_date
  type: object
- description: ''
  name: end_date
  type: object
- description: ''
  name: latest_heartbeat
  type: object
- description: ''
  name: executor_class
  type: object
- description: ''
  name: hostname
  type: object
- description: ''
  name: unixname
  type: object
- description: ''
  name: dag_display_name
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-job-response-schema.json
slug: airflow-job-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: JobResponse
---
