---
description: Describes an Amazon RDS DB snapshot
layout: schema
name: DBSnapshot
properties_list:
- description: The identifier for the DB snapshot
  name: dBSnapshotIdentifier
  type: string
- description: The DB instance identifier of the source DB instance
  name: dBInstanceIdentifier
  type: string
- description: The time when the snapshot was taken
  name: snapshotCreateTime
  type: string
- description: The database engine for the snapshot
  name: engine
  type: string
- description: The version of the database engine
  name: engineVersion
  type: string
- description: The status of the DB snapshot
  name: status
  type: string
- description: The allocated storage size in GiB
  name: allocatedStorage
  type: integer
- description: The port that the database engine was listening on at snapshot time
  name: port
  type: integer
- description: The Availability Zone where the snapshot was created
  name: availabilityZone
  type: string
- description: The VPC ID associated with the DB snapshot
  name: vpcId
  type: string
- description: The time when the source DB instance was created
  name: instanceCreateTime
  type: string
- description: The master username for the DB snapshot
  name: masterUsername
  type: string
- description: The type of the DB snapshot
  name: snapshotType
  type: string
- description: Whether the DB snapshot is encrypted
  name: encrypted
  type: boolean
- description: The storage type associated with the DB snapshot
  name: storageType
  type: string
- description: The Amazon Resource Name (ARN) for the DB snapshot
  name: dBSnapshotArn
  type: string
- description: Tags assigned to the DB snapshot
  name: tags
  type: array
provider_name: Amazon RDS
provider_slug: amazon-rds
schema_file: json-schema/amazon-rds-openapi-db-snapshot-schema.json
slug: amazon-rds-openapi-db-snapshot
tags:
- AWS
- Cloud Databases
- Database Service
- DBaaS
- Managed Databases
- Relational Databases
title: DBSnapshot
---
