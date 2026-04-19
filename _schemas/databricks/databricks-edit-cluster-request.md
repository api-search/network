---
description: ''
layout: schema
name: EditClusterRequest
properties_list:
- description: The unique identifier of the cluster to edit.
  name: cluster_id
  type: string
- description: The new name for the cluster.
  name: cluster_name
  type: string
- description: The runtime version.
  name: spark_version
  type: string
- description: The node type for worker nodes.
  name: node_type_id
  type: string
- description: The node type for the Spark driver.
  name: driver_node_type_id
  type: string
- description: Number of worker nodes.
  name: num_workers
  type: integer
- description: ''
  name: spark_conf
  type: object
- description: ''
  name: custom_tags
  type: object
- description: ''
  name: spark_env_vars
  type: object
- description: ''
  name: autotermination_minutes
  type: integer
- description: ''
  name: enable_elastic_disk
  type: boolean
- description: ''
  name: instance_pool_id
  type: string
- description: ''
  name: policy_id
  type: string
- description: ''
  name: data_security_mode
  type: string
- description: ''
  name: single_user_name
  type: string
- description: ''
  name: runtime_engine
  type: string
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-edit-cluster-request-schema.json
slug: databricks-edit-cluster-request
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
title: EditClusterRequest
---
