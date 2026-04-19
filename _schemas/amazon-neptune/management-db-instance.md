---
description: Contains the details of an Amazon Neptune DB instance.
layout: schema
name: DBInstance
properties_list:
- description: The user-supplied database identifier.
  name: DBInstanceIdentifier
  type: string
- description: The compute and memory capacity of the instance.
  name: DBInstanceClass
  type: string
- description: The database engine (neptune).
  name: Engine
  type: string
- description: Current state of the instance.
  name: DBInstanceStatus
  type: string
- description: ''
  name: Endpoint
  type: object
- description: The cluster this instance belongs to.
  name: DBClusterIdentifier
  type: string
- description: The Availability Zone of the instance.
  name: AvailabilityZone
  type: string
- description: The weekly time range for system maintenance.
  name: PreferredMaintenanceWindow
  type: string
- description: The version of the database engine.
  name: EngineVersion
  type: string
- description: Whether minor version upgrades are applied automatically.
  name: AutoMinorVersionUpgrade
  type: boolean
- description: Whether the instance is publicly accessible.
  name: PubliclyAccessible
  type: boolean
- description: The ARN of the DB instance.
  name: DBInstanceArn
  type: string
- description: The failover priority for the instance.
  name: PromotionTier
  type: integer
- description: Whether the instance storage is encrypted.
  name: StorageEncrypted
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-db-instance-schema.json
slug: management-db-instance
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: DBInstance
---
