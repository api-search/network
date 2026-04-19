---
description: Contains the details of an Amazon Neptune DB cluster.
layout: schema
name: DBCluster
properties_list:
- description: The user-supplied DB cluster identifier.
  name: DBClusterIdentifier
  type: string
- description: The Amazon Resource Name (ARN) for the DB cluster.
  name: DBClusterArn
  type: string
- description: Current state of the cluster.
  name: Status
  type: string
- description: The database engine (neptune).
  name: Engine
  type: string
- description: The version of the database engine.
  name: EngineVersion
  type: string
- description: The connection endpoint for the primary instance.
  name: Endpoint
  type: string
- description: The reader endpoint for read replicas.
  name: ReaderEndpoint
  type: string
- description: The port that the DB cluster listens on.
  name: Port
  type: integer
- description: The master username for the cluster.
  name: MasterUsername
  type: string
- description: The name of the DB cluster parameter group.
  name: DBClusterParameterGroup
  type: string
- description: The DB subnet group associated with the cluster.
  name: DBSubnetGroup
  type: string
- description: The allocated storage size in gigabytes.
  name: AllocatedStorage
  type: integer
- description: The time when the DB cluster was created.
  name: ClusterCreateTime
  type: string
- description: The daily time range for automated backups.
  name: PreferredBackupWindow
  type: string
- description: The weekly time range for system maintenance.
  name: PreferredMaintenanceWindow
  type: string
- description: Whether the cluster is Multi-AZ enabled.
  name: MultiAZ
  type: boolean
- description: Whether the cluster storage is encrypted.
  name: StorageEncrypted
  type: boolean
- description: The KMS key identifier for encrypted clusters.
  name: KmsKeyId
  type: string
- description: Whether deletion protection is enabled.
  name: DeletionProtection
  type: boolean
- description: Whether IAM database authentication is enabled.
  name: IAMDatabaseAuthenticationEnabled
  type: boolean
- description: The list of instances in the cluster.
  name: DBClusterMembers
  type: array
- description: IAM roles associated with the cluster.
  name: AssociatedRoles
  type: array
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-db-cluster-schema.json
slug: management-db-cluster
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: DBCluster
---
