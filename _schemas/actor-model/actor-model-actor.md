---
description: An actor in the system with its current state and mailbox info
layout: schema
name: Actor
properties_list:
- description: Unique actor identifier
  name: id
  type: string
- description: Hierarchical actor path
  name: path
  type: string
- description: Current behavior class or name
  name: behavior
  type: string
- description: Current actor status
  name: status
  type: string
- description: Number of pending messages in mailbox
  name: mailboxSize
  type: integer
- description: Parent supervisor actor ID
  name: supervisorId
  type: string
- description: When the actor was spawned
  name: spawnedAt
  type: string
- description: Timestamp of last processed message
  name: lastMessageAt
  type: string
- description: Total messages processed since spawn
  name: messageCount
  type: integer
- description: Number of times this actor has been restarted
  name: restartCount
  type: integer
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-actor-schema.json
slug: actor-model-actor
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: Actor
---
