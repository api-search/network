---
description: Describes an Amazon Aurora DB cluster
layout: schema
name: DBCluster
properties_list:
- description: The user-supplied identifier for the DB cluster
  name: dBClusterIdentifier
  type: string
- description: The Amazon Resource Name (ARN) for the DB cluster
  name: dBClusterArn
  type: string
- description: The current state of the DB cluster
  name: status
  type: string
- description: The database engine for the DB cluster
  name: engine
  type: string
- description: The version of the database engine
  name: engineVersion
  type: string
- description: The name of the initial database
  name: databaseName
  type: string
- description: The master username for the DB cluster
  name: masterUsername
  type: string
- description: The DNS address of the primary instance of the DB cluster
  name: endpoint
  type: string
- description: The reader endpoint for the DB cluster
  name: readerEndpoint
  type: string
- description: The port that the database engine is listening on
  name: port
  type: integer
- description: The list of DB instances that are part of the cluster
  name: dBClusterMembers
  type: array
- description: The Availability Zones the DB cluster is associated with
  name: availabilityZones
  type: array
- description: The number of days for which automatic DB snapshots are retained
  name: backupRetentionPeriod
  type: integer
- description: Whether the DB cluster is encrypted
  name: storageEncrypted
  type: boolean
- description: Whether the DB cluster has instances in multiple AZs
  name: multiAZ
  type: boolean
- description: The time when the DB cluster was created
  name: clusterCreateTime
  type: string
- description: The current allocated storage size in GiB for the cluster
  name: allocatedStorage
  type: integer
- description: Tags assigned to the DB cluster
  name: tags
  type: array
provider_name: Amazon RDS
provider_slug: amazon-rds
schema_file: json-schema/amazon-rds-openapi-db-cluster-schema.json
slug: amazon-rds-openapi-db-cluster
tags:
- AWS
- Cloud Databases
- Database Service
- DBaaS
- Managed Databases
- Relational Databases
title: DBCluster
---
