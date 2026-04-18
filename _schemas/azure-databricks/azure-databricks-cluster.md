---
description: Schema representing an Azure Databricks cluster configuration and state. A cluster is a set of computation resources and configurations on which you run notebooks, jobs, and libraries. Clusters consist of a driver node and worker nodes running Apache Spark.
layout: schema
name: Azure Databricks Cluster
properties_list:
- description: Canonical identifier for the cluster, assigned by Databricks upon creation.
  name: cluster_id
  type: string
- description: Cluster name requested by the user. This name does not have to be unique. If not specified at creation, the cluster name defaults to an empty string.
  name: cluster_name
  type: string
- description: The Databricks Runtime version for the cluster. Determines the version of Apache Spark and other preinstalled libraries. Use the spark-versions API endpoint to retrieve available versions.
  name: spark_version
  type: string
- description: The Azure VM node type for worker nodes. Determines the amount of memory, CPU cores, and local storage available to each worker. Use the list-node-types API to retrieve available types.
  name: node_type_id
  type: string
- description: The Azure VM node type for the Spark driver node. If not specified, the driver node type defaults to the same value as node_type_id.
  name: driver_node_type_id
  type: string
- description: Number of worker nodes in the cluster. For a fixed-size cluster, set this to the desired number of workers. When autoscale is specified, this field is not used.
  name: num_workers
  type: integer
- description: Parameters for autoscaling the cluster. When specified, the cluster dynamically scales between the minimum and maximum number of workers based on workload.
  name: autoscale
  type: object
- description: An object containing a set of optional, user-specified Spark configuration key-value pairs. These are passed directly to the Spark driver and executors via the --conf flag.
  name: spark_conf
  type: object
- description: Attributes specific to Azure Databricks clusters, controlling Azure-specific behavior such as spot instance configuration.
  name: azure_attributes
  type: object
- description: SSH public key contents that are added to each node in the cluster. You can specify up to 10 keys.
  name: ssh_public_keys
  type: array
- description: Custom tags to apply to cluster resources. These tags are propagated to Azure resources created for the cluster. Databricks adds several default tags in addition to any custom tags specified.
  name: custom_tags
  type: object
- description: Configuration for delivering Spark logs to a long-term storage destination. Only one destination type can be specified.
  name: cluster_log_conf
  type: object
- description: Cluster-scoped init scripts to run when the cluster starts. Init scripts run before the Spark driver or workers start. A maximum of 10 init scripts can be specified.
  name: init_scripts
  type: array
- description: Environment variables to set on the Spark driver and worker processes. Key-value pairs are set as environment variables before the process starts.
  name: spark_env_vars
  type: object
- description: When enabled, the cluster will autoscale local storage. The disk space used by the cluster auto-adjusts based on the amount of data shuffled. Recommended for workloads with varying storage needs.
  name: enable_elastic_disk
  type: boolean
- description: The optional ID of the instance pool to use for cluster nodes. When specified, the cluster uses idle instances from the pool to reduce startup time. Both driver and worker nodes use the same pool unle
  name: instance_pool_id
  type: string
- description: The optional ID of the instance pool to use for the driver node. If specified, the driver uses this pool while workers use instance_pool_id.
  name: driver_instance_pool_id
  type: string
- description: Identifier of the cluster policy used to create the cluster. Cluster policies enforce configuration constraints and provide defaults.
  name: policy_id
  type: string
- description: When enabled, locally attached disks on cluster nodes are encrypted. This includes shuffle data, spilled data, and local caches.
  name: enable_local_disk_encryption
  type: boolean
- description: The runtime engine to use on the cluster. PHOTON provides a native vectorized query engine that accelerates SQL and DataFrame workloads.
  name: runtime_engine
  type: string
- description: The data security mode for the cluster. Controls how data access is governed. USER_ISOLATION provides per-user isolation with Unity Catalog. SINGLE_USER restricts the cluster to a single user.
  name: data_security_mode
  type: string
- description: The optional user name of the user assigned to the cluster when data_security_mode is SINGLE_USER. This user is the only one who can execute commands on the cluster.
  name: single_user_name
  type: string
- description: Current state of the cluster. PENDING indicates the cluster is being created; RUNNING means it is ready for use; TERMINATED means it has been stopped.
  name: state
  type: string
- description: A human-readable message providing additional details about the current state of the cluster.
  name: state_message
  type: string
- description: The username of the user who created the cluster.
  name: creator_user_name
  type: string
- description: Time (in epoch milliseconds) when the cluster was created or last started.
  name: start_time
  type: integer
- description: Time (in epoch milliseconds) when the cluster was terminated.
  name: terminated_time
  type: integer
- description: Time (in epoch milliseconds) when the cluster driver last lost its state. This occurs when the driver node is lost.
  name: last_state_loss_time
  type: integer
- description: Time (in epoch milliseconds) when the cluster last had activity. Inactivity duration is measured from this time for autotermination.
  name: last_activity_time
  type: integer
- description: Automatically terminates the cluster after it has been inactive for this time in minutes. If set to 0, the cluster is not auto-terminated. Default is 120 minutes.
  name: autotermination_minutes
  type: integer
- description: Indicates the source that created the cluster, such as UI, API, or JOB.
  name: cluster_source
  type: string
- description: Tags that are automatically applied by Databricks regardless of custom_tags settings. Includes Vendor, Creator, ClusterId, and ClusterName.
  name: default_tags
  type: object
- description: Information about why the cluster was terminated, available when the cluster is in TERMINATED state.
  name: termination_reason
  type: object
- description: Information about the Spark driver node.
  name: driver
  type: object
- description: Information about the Spark executor (worker) nodes.
  name: executors
  type: array
- description: Port on which the JDBC/ODBC server is listening for connections. Available only when the cluster is running.
  name: jdbc_port
  type: integer
- description: Total amount of memory (in megabytes) available across all nodes in the cluster.
  name: cluster_memory_mb
  type: integer
- description: Total number of CPU cores available across all nodes in the cluster.
  name: cluster_cores
  type: number
- description: Disk specification for the cluster nodes.
  name: disk_spec
  type: object
- description: Status of log delivery for the cluster.
  name: cluster_log_status
  type: object
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-cluster-schema.json
slug: azure-databricks-cluster
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: Azure Databricks Cluster
---
