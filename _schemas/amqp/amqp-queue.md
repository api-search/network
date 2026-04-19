---
description: Schema describing an AMQP 0-9-1 queue. Queues store messages and deliver them to consumers. They can be durable, exclusive, or auto-deleted, and support various arguments for controlling message TTL, length limits, and dead-lettering.
layout: schema
name: AMQP Queue
properties_list:
- description: The name of the queue. An empty string causes the broker to generate a unique name.
  name: name
  type: string
- description: If true, the queue survives broker restarts.
  name: durable
  type: boolean
- description: If true, the queue is used by only one connection and will be deleted when that connection closes.
  name: exclusive
  type: boolean
- description: If true, the queue is automatically deleted when the last consumer unsubscribes.
  name: autoDelete
  type: boolean
- description: Optional arguments for queue declaration providing extended configuration.
  name: arguments
  type: object
provider_name: AMQP
provider_slug: amqp
schema_file: json-schema/amqp-queue.json
slug: amqp-queue
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
title: AMQP Queue
---
