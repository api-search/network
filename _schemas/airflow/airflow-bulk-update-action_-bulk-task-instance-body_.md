---
description: BulkUpdateAction_BulkTaskInstanceBody_ schema from Apache Airflow API
layout: schema
name: BulkUpdateAction_BulkTaskInstanceBody_
properties_list:
- description: The action to be performed on the entities.
  name: action
  type: string
- description: A list of entities to be updated.
  name: entities
  type: array
- description: A list of field names to update for each entity.Only these fields will be applied from the request body to the database model.Any extra fields provided will be ignored.
  name: update_mask
  type: object
- description: ''
  name: action_on_non_existence
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-bulk-update-action_-bulk-task-instance-body_-schema.json
slug: airflow-bulk-update-action_-bulk-task-instance-body_
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: BulkUpdateAction_BulkTaskInstanceBody_
---
