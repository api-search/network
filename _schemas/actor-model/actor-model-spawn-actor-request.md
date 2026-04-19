---
description: Request to spawn a new actor
layout: schema
name: SpawnActorRequest
properties_list:
- description: Behavior class or type name
  name: behavior
  type: string
- description: Optional custom actor ID (auto-generated if omitted)
  name: id
  type: string
- description: Parent supervisor ID
  name: supervisorId
  type: string
- description: Initial state to inject into the actor
  name: initialState
  type: object
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-spawn-actor-request-schema.json
slug: actor-model-spawn-actor-request
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: SpawnActorRequest
---
