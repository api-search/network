---
class_count: 1
classes:
- AMQP Message
context_file: json-ld/amqp-amqp-message-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/json-ld/amqp-amqp-message-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amqp Amqp Message from AMQP.
layout: jsonld
name: Amqp Amqp Message Context
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
  name: properties
  type: string
- container: ''
  name: headers
  type: reference
- container: ''
  name: body
  type: string
- container: ''
  name: exchange
  type: string
- container: ''
  name: routingKey
  type: string
- container: ''
  name: mandatory
  type: boolean
- container: ''
  name: immediate
  type: boolean
property_count: 7
provider_name: AMQP
provider_slug: amqp
slug: amqp-amqp-message-context
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
