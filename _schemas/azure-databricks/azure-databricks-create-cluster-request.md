---
description: ''
layout: schema
name: CreateClusterRequest
properties_list:
- description: Cluster name requested by the user. Does not have to be unique. If not specified at creation, the cluster name is an empty string.
  name: cluster_name
  type: string
- description: The runtime version of the cluster. You can retrieve a list of available runtime versions using the spark-versions endpoint.
  name: spark_version
  type: string
- description: The node type for the worker nodes. Refer to list-node-types for available node types.
  name: node_type_id
  type: string
- description: The node type for the driver node. If unset, the driver node type is set as the same value as node_type_id.
  name: driver_node_type_id
  type: string
- description: Number of worker nodes. For a fixed-size cluster, set this to the desired number of workers. For an autoscaling cluster, this field is ignored in favor of autoscale settings.
  name: num_workers
  type: integer
- description: Map of Spark configuration key-value pairs. These are passed directly to the Spark driver and executors.
  name: spark_conf
  type: object
- description: SSH public keys for accessing cluster nodes
  name: ssh_public_keys
  type: array
- description: Custom tags applied to cluster resources. Databricks adds default tags in addition to any custom tags you specify.
  name: custom_tags
  type: object
- description: Init scripts to run when the cluster starts
  name: init_scripts
  type: array
- description: Map of environment variable key-value pairs for the Spark process.
  name: spark_env_vars
  type: object
- description: If true, enable autoscaling local storage. When enabled, the amount of disk space used by the cluster auto-adjusts.
  name: enable_elastic_disk
  type: boolean
- description: ID of the instance pool to use for cluster nodes. If specified, the cluster uses the instance pool for both driver and worker nodes.
  name: instance_pool_id
  type: string
- description: Identifier of the cluster policy used to create the cluster.
  name: policy_id
  type: string
- description: Whether to enable local disk encryption for the cluster
  name: enable_local_disk_encryption
  type: boolean
- description: The runtime engine to use. PHOTON provides optimized query execution.
  name: runtime_engine
  type: string
- description: Data security mode for the cluster. Determines how data access is controlled.
  name: data_security_mode
  type: string
- description: The name of the single user who can execute commands on the cluster. Required when data_security_mode is SINGLE_USER.
  name: single_user_name
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-create-cluster-request-schema.json
slug: azure-databricks-create-cluster-request
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: CreateClusterRequest
---
