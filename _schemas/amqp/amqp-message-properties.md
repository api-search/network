---
description: Schema describing the standard AMQP 0-9-1 message properties (Basic.Properties). These properties are defined in the AMQP specification and provide metadata about the message content, delivery, and routing.
layout: schema
name: AMQP Message Properties
properties_list:
- description: MIME content type of the message body (e.g., application/json, text/plain).
  name: contentType
  type: string
- description: MIME content encoding of the message body (e.g., utf-8, gzip).
  name: contentEncoding
  type: string
- description: Application-specific message headers as an AMQP field table.
  name: headers
  type: object
- description: Message delivery mode. 1 = non-persistent (may be lost on broker restart), 2 = persistent (written to disk).
  name: deliveryMode
  type: integer
- description: Message priority level from 0 (lowest) to 9 (highest).
  name: priority
  type: integer
- description: Application-defined correlation identifier, typically used to correlate RPC responses with requests.
  name: correlationId
  type: string
- description: Name of the queue to which replies should be sent, used in the request/reply messaging pattern.
  name: replyTo
  type: string
- description: Message expiration (TTL) as a string representing milliseconds. The message will be discarded after this duration.
  name: expiration
  type: string
- description: Application-defined unique message identifier.
  name: messageId
  type: string
- description: Message timestamp as a UNIX epoch timestamp (seconds since 1970-01-01T00:00:00Z).
  name: timestamp
  type: integer
- description: Application-defined message type name, used to describe the kind of message.
  name: type
  type: string
- description: The user ID of the authenticated user who published the message. Validated by the broker against the connection credentials.
  name: userId
  type: string
- description: Application identifier of the publishing application.
  name: appId
  type: string
- description: Cluster identifier for use by clustering applications. Deprecated in AMQP 0-9-1.
  name: clusterId
  type: string
provider_name: AMQP
provider_slug: amqp
schema_file: json-schema/amqp-message-properties.json
slug: amqp-message-properties
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
title: AMQP Message Properties
---
