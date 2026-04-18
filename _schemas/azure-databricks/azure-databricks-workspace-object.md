---
description: ''
layout: schema
name: WorkspaceObject
properties_list:
- description: Type of the workspace object
  name: object_type
  type: string
- description: Absolute path of the object in the workspace
  name: path
  type: string
- description: Programming language of the object. Only applicable for notebooks.
  name: language
  type: string
- description: Unique identifier for the object
  name: object_id
  type: integer
- description: Creation timestamp in epoch milliseconds
  name: created_at
  type: integer
- description: Last modification timestamp in epoch milliseconds
  name: modified_at
  type: integer
- description: Resource ID for the object
  name: resource_id
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-workspace-object-schema.json
slug: azure-databricks-workspace-object
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: WorkspaceObject
---
