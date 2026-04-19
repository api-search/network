---
description: Describes an Amazon RDS DB instance
layout: schema
name: DBInstance
properties_list:
- description: The user-supplied unique key that identifies the DB instance
  name: dBInstanceIdentifier
  type: string
- description: The name of the compute and memory capacity class of the DB instance
  name: dBInstanceClass
  type: string
- description: The database engine for this DB instance
  name: engine
  type: string
- description: The version of the database engine
  name: engineVersion
  type: string
- description: The current state of the DB instance
  name: dBInstanceStatus
  type: string
- description: The master username for the DB instance
  name: masterUsername
  type: string
- description: The name of the initial database provided during creation
  name: dBName
  type: string
- description: The connection endpoint for the DB instance
  name: endpoint
  type: object
- description: The allocated storage size in gibibytes (GiB)
  name: allocatedStorage
  type: integer
- description: The date and time the DB instance was created
  name: instanceCreateTime
  type: string
- description: The daily time range during which automated backups are created
  name: preferredBackupWindow
  type: string
- description: The number of days for which automatic DB snapshots are retained
  name: backupRetentionPeriod
  type: integer
- description: The VPC security groups associated with the DB instance
  name: vpcSecurityGroups
  type: array
- description: The Availability Zone where the DB instance is located
  name: availabilityZone
  type: string
- description: Information about the subnet group associated with the DB instance
  name: dBSubnetGroup
  type: object
- description: Whether the DB instance is a Multi-AZ deployment
  name: multiAZ
  type: boolean
- description: Whether minor version patches are applied automatically
  name: autoMinorVersionUpgrade
  type: boolean
- description: The storage type associated with the DB instance
  name: storageType
  type: string
- description: Whether the DB instance is encrypted
  name: storageEncrypted
  type: boolean
- description: Whether the DB instance is publicly accessible
  name: publiclyAccessible
  type: boolean
- description: The Amazon Resource Name (ARN) for the DB instance
  name: dBInstanceArn
  type: string
- description: Tags assigned to the DB instance
  name: tags
  type: array
provider_name: Amazon RDS
provider_slug: amazon-rds
schema_file: json-schema/amazon-rds-openapi-db-instance-schema.json
slug: amazon-rds-openapi-db-instance
tags:
- AWS
- Cloud Databases
- Database Service
- DBaaS
- Managed Databases
- Relational Databases
title: DBInstance
---
