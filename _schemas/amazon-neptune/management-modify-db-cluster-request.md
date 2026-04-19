---
description: ModifyDBClusterRequest schema from Neptune
layout: schema
name: ModifyDBClusterRequest
properties_list:
- description: The DB cluster identifier.
  name: DBClusterIdentifier
  type: string
- description: The new cluster identifier when renaming.
  name: NewDBClusterIdentifier
  type: string
- description: The version of the Neptune engine to upgrade to.
  name: EngineVersion
  type: string
- description: The port number on which the cluster accepts connections.
  name: Port
  type: integer
- description: The name of the cluster parameter group to use.
  name: DBClusterParameterGroupName
  type: string
- description: ''
  name: VpcSecurityGroupIds
  type: array
- description: ''
  name: BackupRetentionPeriod
  type: integer
- description: ''
  name: PreferredBackupWindow
  type: string
- description: ''
  name: PreferredMaintenanceWindow
  type: string
- description: ''
  name: DeletionProtection
  type: boolean
- description: Whether to apply changes immediately or during the next maintenance window.
  name: ApplyImmediately
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-modify-db-cluster-request-schema.json
slug: management-modify-db-cluster-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: ModifyDBClusterRequest
---
