---
description: Represents an Amazon Neptune DB cluster, which is a managed graph database cluster with one writer instance and up to 15 read replica instances sharing a distributed storage volume.
layout: schema
name: Amazon Neptune DB Cluster
properties_list:
- description: The user-supplied unique identifier for the DB cluster. Must contain 1-63 alphanumeric characters or hyphens, start with a letter, and not end with a hyphen.
  name: DBClusterIdentifier
  type: string
- description: The Amazon Resource Name (ARN) for the DB cluster.
  name: DBClusterArn
  type: string
- description: The current state of the DB cluster.
  name: Status
  type: string
- description: The name of the database engine (always 'neptune').
  name: Engine
  type: string
- description: The version of the Neptune database engine.
  name: EngineVersion
  type: string
- description: The DNS address of the primary instance of the DB cluster. This is the read/write cluster endpoint.
  name: Endpoint
  type: string
- description: The reader endpoint for the DB cluster. Used to distribute read-only connections across read replicas.
  name: ReaderEndpoint
  type: string
- description: The port that the DB cluster listens on.
  name: Port
  type: integer
- description: The name of the DB cluster parameter group associated with the cluster.
  name: DBClusterParameterGroup
  type: string
- description: The name of the DB subnet group associated with the cluster.
  name: DBSubnetGroup
  type: string
- description: The allocated storage size in gibibytes (GiB).
  name: AllocatedStorage
  type: integer
- description: The time when the DB cluster was created, in UTC.
  name: ClusterCreateTime
  type: string
- description: The daily time range during which automated backups are created (UTC), in the format hh24:mi-hh24:mi.
  name: PreferredBackupWindow
  type: string
- description: The weekly time range during which system maintenance can occur (UTC), in the format ddd:hh24:mi-ddd:hh24:mi.
  name: PreferredMaintenanceWindow
  type: string
- description: The number of days for which automated backups are retained.
  name: BackupRetentionPeriod
  type: integer
- description: Whether the DB cluster has instances in multiple Availability Zones.
  name: MultiAZ
  type: boolean
- description: Whether the DB cluster storage is encrypted at rest.
  name: StorageEncrypted
  type: boolean
- description: The AWS KMS key identifier used for encrypting the cluster storage.
  name: KmsKeyId
  type: string
- description: Whether deletion protection is enabled. When enabled, the cluster cannot be deleted.
  name: DeletionProtection
  type: boolean
- description: Whether AWS Identity and Access Management (IAM) database authentication is enabled.
  name: IAMDatabaseAuthenticationEnabled
  type: boolean
- description: The list of DB instances that are members of this cluster.
  name: DBClusterMembers
  type: array
- description: The VPC security groups associated with the cluster.
  name: VpcSecurityGroups
  type: array
- description: IAM roles that are associated with the DB cluster for accessing other AWS services.
  name: AssociatedRoles
  type: array
- description: The Availability Zones in which instances in the cluster can be created.
  name: AvailabilityZones
  type: array
- description: Whether tags are copied to snapshots of the DB cluster.
  name: CopyTagsToSnapshot
  type: boolean
- description: Whether the cluster can be cloned across accounts.
  name: CrossAccountClone
  type: boolean
- description: The scaling configuration for Neptune Serverless.
  name: ServerlessV2ScalingConfiguration
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/amazon-neptune-db-cluster-schema.json
slug: amazon-neptune-db-cluster
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: Amazon Neptune DB Cluster
---
