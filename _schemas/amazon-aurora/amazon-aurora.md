---
description: Schema defining the structure of an Amazon Aurora DB cluster resource, including cluster configuration, instances, endpoints, storage, backup, and security settings.
layout: schema
name: Amazon Aurora DB Cluster
properties_list:
- description: The user-supplied DB cluster identifier.
  name: DBClusterIdentifier
  type: string
- description: The Amazon Resource Name (ARN) for the DB cluster.
  name: DBClusterArn
  type: string
- description: The database engine for the DB cluster.
  name: Engine
  type: string
- description: The version of the database engine.
  name: EngineVersion
  type: string
- description: The current state of the DB cluster.
  name: Status
  type: string
- description: The connection endpoint for the primary instance of the DB cluster.
  name: Endpoint
  type: string
- description: The reader endpoint for the DB cluster.
  name: ReaderEndpoint
  type: string
- description: The port that the database engine is listening on.
  name: Port
  type: integer
- description: The master username for the DB cluster.
  name: MasterUsername
  type: string
- description: The name of the initial database created when the cluster was created.
  name: DatabaseName
  type: string
- description: The list of DB instances that make up the DB cluster.
  name: DBClusterMembers
  type: array
- description: The list of Availability Zones that instances in the DB cluster can be created in.
  name: AvailabilityZones
  type: array
- description: The number of days for which automatic DB snapshots are retained.
  name: BackupRetentionPeriod
  type: integer
- description: The daily time range during which automated backups are created.
  name: PreferredBackupWindow
  type: string
- description: The weekly time range during which system maintenance can occur.
  name: PreferredMaintenanceWindow
  type: string
- description: Whether the DB cluster is encrypted.
  name: StorageEncrypted
  type: boolean
- description: The AWS KMS key identifier for the encrypted DB cluster.
  name: KmsKeyId
  type: string
- description: Whether the DB cluster has deletion protection enabled.
  name: DeletionProtection
  type: boolean
- description: The list of VPC security groups that the DB cluster belongs to.
  name: VpcSecurityGroups
  type: array
- description: The name of the DB subnet group associated with the DB cluster.
  name: DBSubnetGroup
  type: string
- description: The time when the DB cluster was created.
  name: ClusterCreateTime
  type: string
- description: Tags associated with the DB cluster.
  name: Tags
  type: array
provider_name: Amazon Aurora
provider_slug: amazon-aurora
schema_file: json-schema/amazon-aurora-schema.json
slug: amazon-aurora
tags:
- Amazon Aurora
- MySQL
- PostgreSQL
- Relational Database
- AWS
title: Amazon Aurora DB Cluster
---
