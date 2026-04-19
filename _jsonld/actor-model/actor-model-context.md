---
class_count: 53
classes:
- Actor
- ActorList
- ActorMessage
- MailboxInspection
- Supervisor
- ClusterMember
- Shard
- SystemHealth
- id
- path
- behavior
- status
- mailboxSize
- supervisorId
- messageCount
- restartCount
- actors
- total
- cursor
- type
- payload
- replyTo
- correlationId
- priority
- actorId
- pendingCount
- messages
- oldestMessageAge
- strategy
- maxRestarts
- restartWindow
- childCount
- supervisors
- nodeId
- address
- roles
- actorCount
- members
- leader
- totalActors
- shardId
- region
- entityCount
- shards
- totalShards
- totalEntities
- activeActors
- messagesPerSecond
- errorRate
- deadLetters
- clusterSize
- uptime
- initialState
context_file: json-ld/actor-model-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/actor-model/refs/heads/main/json-ld/actor-model-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Actor Model from Actor Model.
layout: jsonld
name: Actor Model Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: actor
  uri: https://vocab.api-evangelist.com/actor-model/
properties:
- container: ''
  name: spawnedAt
  type: dateTime
- container: ''
  name: lastMessageAt
  type: dateTime
- container: ''
  name: upSince
  type: dateTime
property_count: 3
provider_name: Actor Model
provider_slug: actor-model
slug: actor-model-context
tags:
- Actor Model
- Concurrency
- Distributed Systems
- JSON-LD
- Linked Data
- Semantic Web
---
