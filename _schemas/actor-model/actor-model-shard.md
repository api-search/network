---
description: A shard partition in the cluster
layout: schema
name: Shard
properties_list:
- description: Shard identifier
  name: shardId
  type: string
- description: Shard region name
  name: region
  type: string
- description: Node hosting this shard
  name: nodeId
  type: string
- description: Number of entities in this shard
  name: entityCount
  type: integer
- description: Shard status
  name: status
  type: string
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-shard-schema.json
slug: actor-model-shard
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: Shard
---
