---
description: Schema describing the structure of an AMQP 0-9-1 message including properties, headers, and payload. An AMQP message consists of message properties (metadata), application headers, and a binary payload body.
layout: schema
name: AMQP Message
properties_list:
- description: ''
  name: properties
  type: object
- description: Application-specific headers as key-value pairs sent in the message header frame.
  name: headers
  type: object
- description: The message body content. Can be any valid JSON value or a binary payload represented as a base64-encoded string.
  name: body
  type: object
- description: The exchange the message was published to.
  name: exchange
  type: string
- description: The routing key used when publishing the message.
  name: routingKey
  type: string
- description: If true, the server will return an undeliverable message with a Return method. If false, the server silently drops the message.
  name: mandatory
  type: boolean
- description: If true, the server will return an undeliverable message if it cannot be immediately consumed. Deprecated in AMQP 0-9-1.
  name: immediate
  type: boolean
provider_name: AMQP
provider_slug: amqp
schema_file: json-schema/amqp-message.json
slug: amqp-message
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
title: AMQP Message
---
