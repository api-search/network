---
description: Serializer for individual bulk action responses. Represents the outcome of a single bulk operation (create, update, or delete). The response includes a list of successful keys and any errors encountered during the operation. This structure helps users understand which key actions succeeded and which failed.
layout: schema
name: BulkActionResponse
properties_list:
- description: A list of unique id/key representing successful operations.
  name: success
  type: array
- description: A list of errors encountered during the operation, each containing details about the issue.
  name: errors
  type: array
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-bulk-action-response-schema.json
slug: airflow-bulk-action-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: BulkActionResponse
---
