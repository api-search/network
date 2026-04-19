---
description: Inspection of pending messages in an actor's mailbox
layout: schema
name: MailboxInspection
properties_list:
- description: Actor identifier
  name: actorId
  type: string
- description: Total pending messages
  name: pendingCount
  type: integer
- description: ''
  name: messages
  type: array
- description: Age of oldest message in milliseconds
  name: oldestMessageAge
  type: integer
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-mailbox-inspection-schema.json
slug: actor-model-mailbox-inspection
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: MailboxInspection
---
