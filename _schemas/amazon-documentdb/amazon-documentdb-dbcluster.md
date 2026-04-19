---
description: Schema representing an Amazon DocumentDB database cluster, which is a managed MongoDB-compatible document database cluster consisting of one or more instances connected to a shared storage volume.
layout: schema
name: Amazon DocumentDB DBCluster
properties_list:
- description: The user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.
  name: DBClusterIdentifier
  type: string
- description: The Amazon Resource Name (ARN) for the DB cluster.
  name: DBClusterArn
  type: string
- description: Specifies the current state of this DB cluster.
  name: Status
  type: string
- description: The name of the database engine to be used for this DB cluster.
  name: Engine
  type: string
- description: Indicates the database engine version.
  name: EngineVersion
  type: string
- description: The connection endpoint for the primary instance of the DB cluster.
  name: Endpoint
  type: string
- description: The reader endpoint for the DB cluster. The reader endpoint load-balances connections across the read replicas.
  name: ReaderEndpoint
  type: string
- description: Specifies the port that the database engine is listening on.
  name: Port
  type: integer
- description: Contains the master username for the DB cluster.
  name: MasterUsername
  type: string
- description: Specifies information on the subnet group associated with the DB cluster.
  name: DBSubnetGroup
  type: string
- description: Specifies whether the DB cluster is encrypted.
  name: StorageEncrypted
  type: boolean
- description: If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.
  name: KmsKeyId
  type: string
- description: Specifies the number of days for which automatic DB snapshots are retained.
  name: BackupRetentionPeriod
  type: integer
- description: Specifies the daily time range during which automated backups are created.
  name: PreferredBackupWindow
  type: string
- description: Specifies the weekly time range during which system maintenance can occur.
  name: PreferredMaintenanceWindow
  type: string
- description: Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
  name: ClusterCreateTime
  type: string
- description: Provides the list of instances that make up the DB cluster.
  name: DBClusterMembers
  type: array
- description: Provides a list of VPC security groups that the DB cluster belongs to.
  name: VpcSecurityGroups
  type: array
- description: Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled.
  name: DeletionProtection
  type: boolean
- description: A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.
  name: EnabledCloudwatchLogsExports
  type: array
provider_name: Amazon DocumentDB
provider_slug: amazon-documentdb
schema_file: json-schema/amazon-documentdb-dbcluster-schema.json
slug: amazon-documentdb-dbcluster
tags:
- Amazon Web Services
- AWS
- Database
- Document Database
- DocumentDB
- Managed Database
- MongoDB
- NoSQL
title: Amazon DocumentDB DBCluster
---
