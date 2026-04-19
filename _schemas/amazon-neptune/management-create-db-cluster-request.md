---
description: CreateDBClusterRequest schema from Neptune
layout: schema
name: CreateDBClusterRequest
properties_list:
- description: The DB cluster identifier.
  name: DBClusterIdentifier
  type: string
- description: The database engine to use (neptune).
  name: Engine
  type: string
- description: The version of the Neptune engine.
  name: EngineVersion
  type: string
- description: The port number on which the cluster accepts connections.
  name: Port
  type: integer
- description: The name of a DB subnet group.
  name: DBSubnetGroupName
  type: string
- description: A list of VPC security group IDs.
  name: VpcSecurityGroupIds
  type: array
- description: Whether the cluster is encrypted.
  name: StorageEncrypted
  type: boolean
- description: The KMS key identifier for an encrypted cluster.
  name: KmsKeyId
  type: string
- description: The daily time range for automated backups (UTC).
  name: PreferredBackupWindow
  type: string
- description: The weekly time range for maintenance (UTC).
  name: PreferredMaintenanceWindow
  type: string
- description: The number of days for which automated backups are retained (1-35).
  name: BackupRetentionPeriod
  type: integer
- description: Whether to enable deletion protection.
  name: DeletionProtection
  type: boolean
- description: Whether to enable IAM database authentication.
  name: IAMDatabaseAuthenticationEnabled
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-create-db-cluster-request-schema.json
slug: management-create-db-cluster-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateDBClusterRequest
---
