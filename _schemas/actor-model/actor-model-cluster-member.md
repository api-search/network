---
description: A node in the actor system cluster
layout: schema
name: ClusterMember
properties_list:
- description: Unique node identifier
  name: nodeId
  type: string
- description: Network address
  name: address
  type: string
- description: Member status
  name: status
  type: string
- description: Node roles
  name: roles
  type: array
- description: When node joined the cluster
  name: upSince
  type: string
- description: Number of actors hosted on this node
  name: actorCount
  type: integer
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-cluster-member-schema.json
slug: actor-model-cluster-member
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: ClusterMember
---
