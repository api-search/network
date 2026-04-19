---
description: Schema representing a Databricks cluster, which is a managed cloud resource for running data engineering and data science workloads on Apache Spark. Clusters can be configured with fixed or autoscaling worker counts, various node types, and cloud-provider-specific attributes.
layout: schema
name: Databricks Cluster
properties_list:
- description: The unique identifier assigned to the cluster by Databricks. This ID is generated during cluster creation and is used to reference the cluster in all subsequent API calls.
  name: cluster_id
  type: string
- description: A human-readable name for the cluster. This does not need to be unique within the workspace.
  name: cluster_name
  type: string
- description: The Databricks Runtime version of the cluster, which determines the versions of Apache Spark, Scala, Java, Python, R, and installed libraries. Use the Runtime Versions API to retrieve available versio
  name: spark_version
  type: string
- description: The cloud provider instance type for worker nodes. Determines the compute and memory resources available to each worker.
  name: node_type_id
  type: string
- description: The cloud provider instance type for the Spark driver node. If not specified, defaults to the same value as node_type_id.
  name: driver_node_type_id
  type:
  - string
  - 'null'
- description: The number of worker nodes in a fixed-size cluster. A cluster has one Spark driver and num_workers executors. Set to 0 for a single-node cluster where the driver acts as both driver and worker.
  name: num_workers
  type: integer
- description: Autoscaling configuration. When set, num_workers is ignored and the cluster dynamically scales between min_workers and max_workers based on workload.
  name: autoscale
  type:
  - object
  - 'null'
- description: The current state of the cluster in its lifecycle.
  name: state
  type: string
- description: A human-readable message providing additional information about the current cluster state, such as the reason for termination.
  name: state_message
  type: string
- description: The time when the cluster was started, represented as epoch milliseconds (Unix timestamp in milliseconds).
  name: start_time
  type: integer
- description: The time when the cluster was terminated, represented as epoch milliseconds.
  name: terminated_time
  type: integer
- description: The time when the cluster driver last lost its state, represented as epoch milliseconds. This occurs when the driver node is lost or restarted.
  name: last_state_loss_time
  type: integer
- description: The time of the last user activity on the cluster, used for auto-termination calculations. Represented as epoch milliseconds.
  name: last_activity_time
  type: integer
- description: The time when the cluster was last restarted, represented as epoch milliseconds.
  name: last_restarted_time
  type: integer
- description: The email address of the user who created the cluster.
  name: creator_user_name
  type: string
- description: The source that initiated the creation of this cluster.
  name: cluster_source
  type: string
- description: A map of Spark configuration key-value pairs that override the default Spark configuration values for this cluster.
  name: spark_conf
  type: object
- description: Additional tags applied to the cluster resources. Tags are propagated to the underlying cloud provider instances for cost tracking and resource management.
  name: custom_tags
  type: object
- description: Environment variables set for all Spark processes running on this cluster. Use the syntax {{secrets/scope/key}} to reference Databricks secrets.
  name: spark_env_vars
  type: object
- description: The number of minutes of inactivity after which the cluster is automatically terminated. A value of 0 disables auto-termination. Default is 120 minutes.
  name: autotermination_minutes
  type: integer
- description: Whether autoscaling local storage is enabled. When enabled, Databricks monitors disk usage on Spark workers and automatically attaches additional disks when needed.
  name: enable_elastic_disk
  type: boolean
- description: The ID of the instance pool to use for cluster nodes. Instance pools reduce cluster start time by maintaining idle, ready-to-use instances.
  name: instance_pool_id
  type:
  - string
  - 'null'
- description: The ID of the cluster policy applied to this cluster. Cluster policies constrain configuration settings and enforce organizational governance.
  name: policy_id
  type:
  - string
  - 'null'
- description: Whether data stored on local disks is encrypted.
  name: enable_local_disk_encryption
  type: boolean
- description: The data security mode of the cluster, which determines how data access is controlled.
  name: data_security_mode
  type: string
- description: The user name (email) of the single user when data_security_mode is SINGLE_USER.
  name: single_user_name
  type:
  - string
  - 'null'
- description: The runtime engine to use. PHOTON enables the Photon vectorized query engine for significantly faster performance on SQL and DataFrame workloads.
  name: runtime_engine
  type: string
- description: AWS-specific attributes for clusters running on Amazon Web Services.
  name: aws_attributes
  type:
  - object
  - 'null'
- description: Azure-specific attributes for clusters running on Microsoft Azure.
  name: azure_attributes
  type:
  - object
  - 'null'
- description: GCP-specific attributes for clusters running on Google Cloud Platform.
  name: gcp_attributes
  type:
  - object
  - 'null'
- description: Initialization scripts that run on each node when the cluster starts. Scripts can be stored in workspace files, Unity Catalog volumes, or DBFS.
  name: init_scripts
  type: array
- description: Default tags automatically applied by Databricks, including Vendor, Creator, ClusterName, and ClusterId.
  name: default_tags
  type: object
- description: The reason the cluster was terminated, including error codes and parameters.
  name: termination_reason
  type:
  - object
  - 'null'
- description: Information about the Spark driver node.
  name: driver
  type:
  - object
  - 'null'
- description: Information about the Spark executor (worker) nodes.
  name: executors
  type: array
- description: The port number on the driver node that serves JDBC/ODBC connections.
  name: jdbc_port
  type: integer
- description: The canonical Spark context identifier for this cluster.
  name: spark_context_id
  type: integer
- description: SSH public keys added to each Spark node in this cluster for SSH access.
  name: ssh_public_keys
  type: array
- description: Disk specifications for the cluster nodes.
  name: disk_spec
  type:
  - object
  - 'null'
- description: Status of cluster log delivery.
  name: cluster_log_status
  type:
  - object
  - 'null'
provider_name: Databricks
provider_slug: databricks
schema_file: json-schema/databricks-cluster-schema.json
slug: databricks-cluster
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
title: Databricks Cluster
---
