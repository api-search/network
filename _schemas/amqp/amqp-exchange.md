---
description: Schema describing an AMQP 0-9-1 exchange. Exchanges receive messages from producers and route them to queues based on the exchange type and binding rules. The four standard exchange types are direct, topic, fanout, and headers.
layout: schema
name: AMQP Exchange
properties_list:
- description: The name of the exchange. The empty string denotes the default (nameless) direct exchange.
  name: name
  type: string
- description: The exchange type which determines the routing algorithm.
  name: type
  type: string
- description: If true, the exchange survives broker restarts. Non-durable exchanges are deleted on restart.
  name: durable
  type: boolean
- description: If true, the exchange is automatically deleted when the last queue is unbound from it.
  name: autoDelete
  type: boolean
- description: If true, the exchange cannot be directly published to by clients; it can only receive messages from other exchanges via exchange-to-exchange bindings.
  name: internal
  type: boolean
- description: Optional arguments for exchange declaration, used for broker-specific extensions (e.g., alternate exchange).
  name: arguments
  type: object
provider_name: AMQP
provider_slug: amqp
schema_file: json-schema/amqp-exchange.json
slug: amqp-exchange
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
title: AMQP Exchange
---
