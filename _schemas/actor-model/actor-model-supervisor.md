---
description: A supervisor actor managing a set of child actors
layout: schema
name: Supervisor
properties_list:
- description: Supervisor actor ID
  name: id
  type: string
- description: Actor path
  name: path
  type: string
- description: Supervision strategy
  name: strategy
  type: string
- description: Maximum restart attempts within window
  name: maxRestarts
  type: integer
- description: Restart window in seconds
  name: restartWindow
  type: integer
- description: Current number of supervised children
  name: childCount
  type: integer
- description: Supervisor status
  name: status
  type: string
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-supervisor-schema.json
slug: actor-model-supervisor
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: Supervisor
---
