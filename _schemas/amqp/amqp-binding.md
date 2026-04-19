---
description: Schema describing an AMQP 0-9-1 binding. Bindings are rules that exchanges use to route messages to queues. A binding links a queue to an exchange with a routing key and optional arguments for headers-based matching.
layout: schema
name: AMQP Binding
properties_list:
- description: The name of the exchange from which messages are routed.
  name: source
  type: string
- description: The name of the queue or exchange to which messages are routed.
  name: destination
  type: string
- description: Whether the destination is a queue or an exchange.
  name: destinationType
  type: string
- description: 'The routing key for the binding. For topic exchanges, supports wildcards: * matches one word, # matches zero or more words.'
  name: routingKey
  type: string
- description: Optional arguments for the binding. Used primarily with headers exchanges for matching on message header values.
  name: arguments
  type: object
provider_name: AMQP
provider_slug: amqp
schema_file: json-schema/amqp-binding.json
slug: amqp-binding
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
title: AMQP Binding
---
