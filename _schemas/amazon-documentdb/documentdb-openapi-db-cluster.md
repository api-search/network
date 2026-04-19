---
description: DBCluster schema from Amazon DocumentDB API
layout: schema
name: DBCluster
properties_list:
- description: The identifier of the DB cluster.
  name: DBClusterIdentifier
  type: string
- description: The Amazon Resource Name (ARN) for the DB cluster.
  name: DBClusterArn
  type: string
- description: Specifies the current state of this DB cluster.
  name: Status
  type: string
- description: The database engine used for this DB cluster.
  name: Engine
  type: string
- description: The version of the database engine.
  name: EngineVersion
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
- description: The DB subnet group associated with the DB cluster.
  name: DBSubnetGroup
  type: string
- description: Specifies whether the DB cluster is encrypted.
  name: StorageEncrypted
  type: boolean
- description: The number of days for which automatic DB snapshots are retained.
  name: BackupRetentionPeriod
  type: integer
- description: The time when the DB cluster was created.
  name: ClusterCreateTime
  type: string
- description: The list of instances that make up the DB cluster.
  name: DBClusterMembers
  type: array
provider_name: Amazon DocumentDB
provider_slug: amazon-documentdb
schema_file: json-schema/documentdb-openapi-db-cluster-schema.json
slug: documentdb-openapi-db-cluster
tags:
- Amazon Web Services
- AWS
- Database
- Document Database
- DocumentDB
- Managed Database
- MongoDB
- NoSQL
title: DBCluster
---
