---
class_count: 1
classes:
- AMQP Message Properties
context_file: json-ld/amqp-amqp-message-properties-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/json-ld/amqp-amqp-message-properties-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amqp Amqp Message Properties from AMQP.
layout: jsonld
name: Amqp Amqp Message Properties Context
namespaces:
- prefix: amqp
  uri: https://www.amqp.org/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: contentType
  type: string
- container: ''
  name: contentEncoding
  type: string
- container: ''
  name: headers
  type: reference
- container: ''
  name: deliveryMode
  type: integer
- container: ''
  name: priority
  type: integer
- container: ''
  name: correlationId
  type: string
- container: ''
  name: replyTo
  type: string
- container: ''
  name: expiration
  type: string
- container: ''
  name: messageId
  type: string
- container: ''
  name: timestamp
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: appId
  type: string
- container: ''
  name: clusterId
  type: string
property_count: 14
provider_name: AMQP
provider_slug: amqp
slug: amqp-amqp-message-properties-context
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
- JSON-LD
- Linked Data
- Semantic Web
---
