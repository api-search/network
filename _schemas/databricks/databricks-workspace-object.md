---
description: ''
layout: schema
name: WorkspaceObject
properties_list:
- description: The type of the workspace object.
  name: object_type
  type: string
- description: The absolute path of the object in the workspace.
  name: path
  type: string
- description: The language of the notebook, if applicable. Only present for notebook objects.
  name: language
  type: string
- description: The unique identifier of the object.
  name: object_id
  type: integer
- description: The creation time in epoch milliseconds.
  name: created_at
  type: integer
- description: The last modified time in epoch milliseconds.
  name: modified_at
  type: integer
- description: Unique identifier for SCIM compliance.
  name: resource_id
  type: string
- description: The file size in bytes (for FILE objects).
  name: size
  type: integer
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-workspace-object-schema.json
slug: databricks-workspace-object
tags:
- AI
- Analytics
- Apache Spark
- Big Data
- Clean Rooms
- Cloud Computing
- Data
- Data Analytics
- Data Engineering
- Data Governance
- Delta Lake
- Delta Sharing
- ETL
- Identity Management
- Lakehouse
- Machine Learning
- MLflow
- Model Serving
- Security
- SQL
- Unity Catalog
- Vector Search
- Visualize
title: WorkspaceObject
---
