---
description: Represents an Amazon Neptune DB instance, which is a compute node within a Neptune DB cluster that processes graph queries and manages the connection to the shared cluster storage.
layout: schema
name: Amazon Neptune DB Instance
properties_list:
- description: The user-supplied unique identifier for the DB instance.
  name: DBInstanceIdentifier
  type: string
- description: The Amazon Resource Name (ARN) for the DB instance.
  name: DBInstanceArn
  type: string
- description: The compute and memory capacity of the DB instance (e.g., db.r5.large, db.r6g.xlarge, db.serverless).
  name: DBInstanceClass
  type: string
- description: The name of the database engine.
  name: Engine
  type: string
- description: The version of the Neptune database engine.
  name: EngineVersion
  type: string
- description: The current state of the DB instance.
  name: DBInstanceStatus
  type: string
- description: The connection endpoint for the DB instance.
  name: Endpoint
  type: object
- description: The identifier of the DB cluster that this instance belongs to.
  name: DBClusterIdentifier
  type: string
- description: The name of the Availability Zone where the DB instance is located.
  name: AvailabilityZone
  type: string
- description: The DB subnet group associated with the instance.
  name: DBSubnetGroup
  type: object
- description: The weekly time range during which system maintenance can occur (UTC).
  name: PreferredMaintenanceWindow
  type: string
- description: Whether minor engine version upgrades are applied automatically.
  name: AutoMinorVersionUpgrade
  type: boolean
- description: Whether the DB instance is publicly accessible.
  name: PubliclyAccessible
  type: boolean
- description: The order in which a read replica is promoted to the primary instance during a failover.
  name: PromotionTier
  type: integer
- description: Whether the DB instance storage is encrypted.
  name: StorageEncrypted
  type: boolean
- description: The AWS KMS key identifier for the encrypted instance.
  name: KmsKeyId
  type: string
- description: The AWS Region-unique, immutable identifier for the DB instance.
  name: DbiResourceId
  type: string
- description: The identifier of the CA certificate for this DB instance.
  name: CACertificateIdentifier
  type: string
- description: Whether tags are copied to snapshots of the DB instance.
  name: CopyTagsToSnapshot
  type: boolean
- description: The date and time when the DB instance was created.
  name: InstanceCreateTime
  type: string
- description: Changes to the DB instance that are pending application.
  name: PendingModifiedValues
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/amazon-neptune-db-instance-schema.json
slug: amazon-neptune-db-instance
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: Amazon Neptune DB Instance
---
