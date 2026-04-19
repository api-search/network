---
description: 'Task instance collection response supporting both offset and cursor pagination. A single flat model is used instead of a discriminated union (``Annotated[Offset | Cursor, Field(discriminator=...)]``) because the OpenAPI ``oneOf`` + ``discriminator`` construct is not handled correctly by ``@hey-api/openapi-ts`` / ``@7nohe/openapi-react-query-codegen``: return types degrade to ``unknown`` in JSDoc and can produce incorrect TypeScript types (see hey-api/openapi-ts#1613, #3270).'
layout: schema
name: TaskInstanceCollectionResponse
properties_list:
- description: ''
  name: task_instances
  type: array
- description: Total number of matching items. Populated for offset pagination, ``null`` when using cursor pagination.
  name: total_entries
  type: object
- description: Token pointing to the next page. Populated for cursor pagination, ``null`` when using offset pagination or when there is no next page.
  name: next_cursor
  type: object
- description: Token pointing to the previous page. Populated for cursor pagination, ``null`` when using offset pagination or when on the first page.
  name: previous_cursor
  type: object
provider_name: Apache Airflow
provider_slug: airflow
schema_file: json-schema/airflow-task-instance-collection-response-schema.json
slug: airflow-task-instance-collection-response
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
title: TaskInstanceCollectionResponse
---
