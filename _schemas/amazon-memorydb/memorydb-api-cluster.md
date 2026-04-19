---
description: An Amazon MemoryDB cluster.
layout: schema
name: Cluster
properties_list:
- description: The Amazon Resource Name (ARN) of the cluster.
  name: ARN
  type: string
- description: Indicates if the cluster has a Multi-AZ configuration.
  name: AvailabilityMode
  type: string
- description: A description of the cluster.
  name: Description
  type: string
- description: The Redis engine version the cluster is running.
  name: EngineVersion
  type: string
- description: The user-supplied name of the cluster.
  name: Name
  type: string
- description: The cluster's node type.
  name: NodeType
  type: string
- description: The number of shards in the cluster.
  name: NumberOfShards
  type: integer
- description: The status of the cluster.
  name: Status
  type: string
- description: A flag to indicate if In-transit encryption is enabled.
  name: TLSEnabled
  type: boolean
provider_name: Amazon MemoryDB
provider_slug: amazon-memorydb
schema_file: json-schema/memorydb-api-cluster-schema.json
slug: memorydb-api-cluster
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Cluster
---
