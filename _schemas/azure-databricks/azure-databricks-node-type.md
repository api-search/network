---
description: ''
layout: schema
name: NodeType
properties_list:
- description: Unique identifier for the node type
  name: node_type_id
  type: string
- description: Memory in megabytes
  name: memory_mb
  type: integer
- description: Number of CPU cores
  name: num_cores
  type: number
- description: Human-readable description
  name: description
  type: string
- description: Azure instance type identifier
  name: instance_type_id
  type: string
- description: Whether the node type is deprecated
  name: is_deprecated
  type: boolean
- description: Number of GPUs available
  name: num_gpus
  type: integer
- description: Category of the node type (General Purpose, Memory Optimized, etc.)
  name: category
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-node-type-schema.json
slug: azure-databricks-node-type
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: NodeType
---
