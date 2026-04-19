---
description: Schema for an Amazon Redshift provisioned cluster resource, representing a fully managed petabyte-scale data warehouse in the AWS cloud. Includes cluster configuration, networking, security, and operational metadata as described in the Amazon Redshift Management Guide.
layout: schema
name: Amazon Redshift Cluster
properties_list:
- description: The unique identifier of the cluster. Must be lowercase, begin with a letter, contain only alphanumeric characters and hyphens, and be between 1 and 63 characters.
  name: ClusterIdentifier
  type: string
- description: The current state of the cluster
  name: ClusterStatus
  type: string
- description: The availability status of the cluster for queries
  name: ClusterAvailabilityStatus
  type: string
- description: The node type for the nodes in the cluster
  name: NodeType
  type: string
- description: The number of compute nodes in the cluster. For single-node clusters this is 1.
  name: NumberOfNodes
  type: integer
- description: The type of the cluster based on number of nodes
  name: ClusterType
  type: string
- description: The name of the initial database created when the cluster was provisioned. Default is 'dev'.
  name: DBName
  type: string
- description: The admin user name for the cluster. Must be lowercase, begin with a letter, contain only alphanumeric characters, and be between 1 and 128 characters.
  name: MasterUsername
  type: string
- description: ''
  name: Endpoint
  type: object
- description: The date and time that the cluster was created
  name: ClusterCreateTime
  type: string
- description: The number of days that automatic cluster snapshots are retained. Default is 1.
  name: AutomatedSnapshotRetentionPeriod
  type: integer
- description: The default number of days to retain a manual snapshot. -1 means indefinitely.
  name: ManualSnapshotRetentionPeriod
  type: integer
- description: List of cluster security groups associated with the cluster
  name: ClusterSecurityGroups
  type: array
- description: List of VPC security groups associated with the cluster
  name: VpcSecurityGroups
  type: array
- description: List of cluster parameter groups associated with this cluster
  name: ClusterParameterGroups
  type: array
- description: The name of the subnet group associated with the cluster
  name: ClusterSubnetGroupName
  type: string
- description: The identifier of the VPC the cluster is in
  name: VpcId
  type: string
- description: The name of the Availability Zone in which the cluster is located
  name: AvailabilityZone
  type: string
- description: The weekly time range for system maintenance in UTC, formatted as ddd:hh24:mi-ddd:hh24:mi
  name: PreferredMaintenanceWindow
  type: string
- description: The version ID of the Amazon Redshift engine running on the cluster
  name: ClusterVersion
  type: string
- description: Whether major version upgrades are applied automatically during the maintenance window
  name: AllowVersionUpgrade
  type: boolean
- description: Whether the cluster can be accessed from a public network
  name: PubliclyAccessible
  type: boolean
- description: Whether data in the cluster is encrypted at rest
  name: Encrypted
  type: boolean
- description: The AWS KMS key ID used for encryption of data at rest
  name: KmsKeyId
  type: string
- description: Whether enhanced VPC routing is enabled, forcing all COPY and UNLOAD traffic through the VPC
  name: EnhancedVpcRouting
  type: boolean
- description: List of IAM roles associated with the cluster for authorization
  name: IamRoles
  type: array
- description: The name of the maintenance track for the cluster
  name: MaintenanceTrackName
  type: string
- description: The number of nodes that you can resize the cluster to using elastic resize
  name: ElasticResizeNumberOfNodeOptions
  type: string
- description: ''
  name: AquaConfiguration
  type: object
- description: The total storage capacity of the cluster in megabytes
  name: TotalStorageCapacityInMegaBytes
  type: integer
- description: The namespace ARN of the cluster
  name: ClusterNamespaceArn
  type: string
- description: Tags associated with the cluster
  name: Tags
  type: array
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-cluster-schema.json
slug: amazon-redshift-cluster
tags:
- Analytics
- Big Data
- Cloud
- Data Lake
- Data Warehouse
- ETL
- Machine Learning
- Serverless
- SQL
title: Amazon Redshift Cluster
---
