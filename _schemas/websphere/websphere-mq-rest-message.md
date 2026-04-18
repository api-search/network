---
description: ''
layout: schema
name: Message
properties_list:
- description: Message identifier
  name: messageId
  type: string
- description: Correlation identifier
  name: correlationId
  type: string
- description: Time the message was put
  name: putDateTime
  type: string
- description: ''
  name: persistence
  type: string
- description: Reply-to queue name
  name: replyToQueue
  type: string
- description: Reply-to queue manager name
  name: replyToQueueManager
  type: string
- description: Message expiry in tenths of a second
  name: expiry
  type: integer
- description: Message body content
  name: body
  type: string
- description: Message format
  name: format
  type: string
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-mq-rest-message-schema.json
slug: websphere-mq-rest-message
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: Message
---
