---
description: ''
layout: schema
name: ClusterInfo
properties_list:
- description: Canonical identifier for the cluster
  name: cluster_id
  type: string
- description: Name of the cluster
  name: cluster_name
  type: string
- description: Databricks Runtime version
  name: spark_version
  type: string
- description: Node type for worker nodes
  name: node_type_id
  type: string
- description: Node type for the driver node
  name: driver_node_type_id
  type: string
- description: Number of worker nodes
  name: num_workers
  type: integer
- description: Current state of the cluster
  name: state
  type: string
- description: Message associated with the current state
  name: state_message
  type: string
- description: Username of the cluster creator
  name: creator_user_name
  type: string
- description: Time when the cluster was started (epoch milliseconds)
  name: start_time
  type: integer
- description: Time when the cluster was terminated (epoch milliseconds)
  name: terminated_time
  type: integer
- description: Time when the cluster driver lost its state (epoch milliseconds)
  name: last_state_loss_time
  type: integer
- description: Time when the cluster last had activity (epoch milliseconds)
  name: last_activity_time
  type: integer
- description: Automatically terminates the cluster after it is inactive for this time in minutes. 0 indicates no autotermination.
  name: autotermination_minutes
  type: integer
- description: Indicates the source that created the cluster
  name: cluster_source
  type: string
- description: Spark configuration key-value pairs
  name: spark_conf
  type: object
- description: ''
  name: custom_tags
  type: object
- description: ''
  name: init_scripts
  type: array
- description: ''
  name: spark_env_vars
  type: object
- description: ''
  name: enable_elastic_disk
  type: boolean
- description: ''
  name: instance_pool_id
  type: string
- description: ''
  name: policy_id
  type: string
- description: Tags applied automatically by Databricks
  name: default_tags
  type: object
- description: ''
  name: cluster_log_status
  type: object
- description: ''
  name: termination_reason
  type: object
- description: ''
  name: data_security_mode
  type: string
- description: ''
  name: single_user_name
  type: string
- description: ''
  name: runtime_engine
  type: string
- description: ''
  name: disk_spec
  type: object
- description: ''
  name: executors
  type: array
- description: Port on which the JDBC/ODBC server is listening
  name: jdbc_port
  type: integer
- description: Total memory in the cluster in megabytes
  name: cluster_memory_mb
  type: integer
- description: Total number of CPU cores in the cluster
  name: cluster_cores
  type: number
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-cluster-info-schema.json
slug: azure-databricks-cluster-info
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: ClusterInfo
---
