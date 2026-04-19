---
description: Contains the details of a Neptune DB cluster snapshot.
layout: schema
name: DBClusterSnapshot
properties_list:
- description: The identifier of the cluster snapshot.
  name: DBClusterSnapshotIdentifier
  type: string
- description: The cluster identifier of the source cluster.
  name: DBClusterIdentifier
  type: string
- description: ''
  name: SnapshotCreateTime
  type: string
- description: ''
  name: Engine
  type: string
- description: ''
  name: EngineVersion
  type: string
- description: The status of the snapshot.
  name: Status
  type: string
- description: ''
  name: AllocatedStorage
  type: integer
- description: ''
  name: VpcId
  type: string
- description: ''
  name: Port
  type: integer
- description: ''
  name: StorageEncrypted
  type: boolean
- description: ''
  name: KmsKeyId
  type: string
- description: ''
  name: DBClusterSnapshotArn
  type: string
- description: The type of the snapshot (manual or automated).
  name: SnapshotType
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-db-cluster-snapshot-schema.json
slug: management-db-cluster-snapshot
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: DBClusterSnapshot
---
