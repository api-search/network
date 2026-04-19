---
description: ''
layout: schema
name: CreateClusterRequest
properties_list:
- description: A human-readable name for the cluster. This does not need to be unique.
  name: cluster_name
  type: string
- description: The runtime version of the cluster. You can retrieve a list of available runtime versions using the Runtime Versions API.
  name: spark_version
  type: string
- description: The node type for worker nodes. This field determines the cloud provider instance type.
  name: node_type_id
  type: string
- description: The node type for the Spark driver. If not specified, defaults to the same value as node_type_id.
  name: driver_node_type_id
  type: string
- description: Number of worker nodes for a fixed-size cluster. A cluster has one Spark driver and num_workers executors. Set to 0 for a single-node cluster.
  name: num_workers
  type: integer
- description: A map of Spark configuration key-value pairs. These override the default Spark configuration values.
  name: spark_conf
  type: object
- description: Additional tags for cluster resources. Tags are propagated to the cloud provider for cost tracking.
  name: custom_tags
  type: object
- description: Environment variables for all Spark processes. Use {{secrets/scope/key}} to reference secrets.
  name: spark_env_vars
  type: object
- description: Minutes of inactivity after which the cluster is automatically terminated. 0 disables auto-termination.
  name: autotermination_minutes
  type: integer
- description: Whether to autoscale local storage. When enabled, Databricks monitors disk usage and attaches additional disks as needed.
  name: enable_elastic_disk
  type: boolean
- description: The optional ID of the instance pool to use for cluster nodes.
  name: instance_pool_id
  type: string
- description: The ID of the cluster policy to apply. Cluster policies constrain the configuration settings.
  name: policy_id
  type: string
- description: Whether to encrypt data on local disks.
  name: enable_local_disk_encryption
  type: boolean
- description: The runtime engine. PHOTON enables the Photon vectorized query engine for faster performance.
  name: runtime_engine
  type: string
- description: Data security mode for the cluster.
  name: data_security_mode
  type: string
- description: The user name (email) of the single user for SINGLE_USER access mode.
  name: single_user_name
  type: string
- description: Init scripts to run when the cluster starts.
  name: init_scripts
  type: array
- description: SSH public keys to add to each Spark node.
  name: ssh_public_keys
  type: array
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-create-cluster-request-schema.json
slug: databricks-create-cluster-request
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
title: CreateClusterRequest
---
