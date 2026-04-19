---
description: CreateDBInstanceRequest schema from Neptune
layout: schema
name: CreateDBInstanceRequest
properties_list:
- description: The DB instance identifier.
  name: DBInstanceIdentifier
  type: string
- description: The compute and memory capacity of the instance.
  name: DBInstanceClass
  type: string
- description: The database engine to use (neptune).
  name: Engine
  type: string
- description: The identifier of the DB cluster to add the instance to.
  name: DBClusterIdentifier
  type: string
- description: The Availability Zone for the instance.
  name: AvailabilityZone
  type: string
- description: ''
  name: PreferredMaintenanceWindow
  type: string
- description: ''
  name: AutoMinorVersionUpgrade
  type: boolean
- description: Failover priority (0-15).
  name: PromotionTier
  type: integer
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-create-db-instance-request-schema.json
slug: management-create-db-instance-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateDBInstanceRequest
---
