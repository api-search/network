---
description: Paginated list of actors
layout: schema
name: ActorList
properties_list:
- description: ''
  name: actors
  type: array
- description: Total actor count
  name: total
  type: integer
- description: Cursor for next page
  name: cursor
  type: string
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-actor-list-schema.json
slug: actor-model-actor-list
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: ActorList
---
