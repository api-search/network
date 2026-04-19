---
description: List of cluster members
layout: schema
name: ClusterMemberList
properties_list:
- description: ''
  name: members
  type: array
- description: Current cluster leader node ID
  name: leader
  type: string
- description: Total actors across all cluster members
  name: totalActors
  type: integer
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-cluster-member-list-schema.json
slug: actor-model-cluster-member-list
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: ClusterMemberList
---
