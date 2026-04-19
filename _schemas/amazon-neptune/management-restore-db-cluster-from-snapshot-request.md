---
description: RestoreDBClusterFromSnapshotRequest schema from Neptune
layout: schema
name: RestoreDBClusterFromSnapshotRequest
properties_list:
- description: The name of the new DB cluster.
  name: DBClusterIdentifier
  type: string
- description: The identifier of the snapshot to restore from.
  name: SnapshotIdentifier
  type: string
- description: The database engine to use.
  name: Engine
  type: string
- description: ''
  name: EngineVersion
  type: string
- description: ''
  name: Port
  type: integer
- description: ''
  name: DBSubnetGroupName
  type: string
- description: ''
  name: VpcSecurityGroupIds
  type: array
- description: ''
  name: DeletionProtection
  type: boolean
- description: ''
  name: IAMDatabaseAuthenticationEnabled
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-restore-db-cluster-from-snapshot-request-schema.json
slug: management-restore-db-cluster-from-snapshot-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: RestoreDBClusterFromSnapshotRequest
---
