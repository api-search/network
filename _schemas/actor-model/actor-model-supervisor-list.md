---
description: Paginated list of supervisors
layout: schema
name: SupervisorList
properties_list:
- description: ''
  name: supervisors
  type: array
- description: Total supervisor count
  name: total
  type: integer
- description: Cursor for next page
  name: cursor
  type: string
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-supervisor-list-schema.json
slug: actor-model-supervisor-list
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: SupervisorList
---
