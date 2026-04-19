---
description: CreateClusterRequest schema from Amazon MemoryDB API
layout: schema
name: CreateClusterRequest
properties_list:
- description: The name of the Access Control List to associate with the cluster.
  name: ACLName
  type: string
- description: The name of the cluster.
  name: ClusterName
  type: string
- description: An optional description of the cluster.
  name: Description
  type: string
- description: The version number of the Redis engine to use.
  name: EngineVersion
  type: string
- description: The compute and memory capacity of the nodes.
  name: NodeType
  type: string
- description: The number of replicas to apply to each shard.
  name: NumReplicasPerShard
  type: integer
- description: The number of shards the cluster will contain.
  name: NumShards
  type: integer
- description: A flag to enable in-transit encryption.
  name: TLSEnabled
  type: boolean
provider_name: Amazon MemoryDB
provider_slug: amazon-memorydb
schema_file: json-schema/memorydb-api-create-cluster-request-schema.json
slug: memorydb-api-create-cluster-request
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: CreateClusterRequest
---
