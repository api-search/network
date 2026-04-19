---
description: A message to be placed in an actor's mailbox
layout: schema
name: ActorMessage
properties_list:
- description: Message type discriminator
  name: type
  type: string
- description: Message payload
  name: payload
  type: object
- description: Actor ID to send reply to (optional)
  name: replyTo
  type: string
- description: Correlation ID for tracing
  name: correlationId
  type: string
- description: Message priority in mailbox
  name: priority
  type: string
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-actor-message-schema.json
slug: actor-model-actor-message
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: ActorMessage
---
