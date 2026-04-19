---
class_count: 1
classes:
- AMQP Exchange
context_file: json-ld/amqp-amqp-exchange-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/json-ld/amqp-amqp-exchange-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amqp Amqp Exchange from AMQP.
layout: jsonld
name: Amqp Amqp Exchange Context
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
  name: name
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: durable
  type: boolean
- container: ''
  name: autoDelete
  type: boolean
- container: ''
  name: internal
  type: boolean
- container: ''
  name: arguments
  type: reference
property_count: 6
provider_name: AMQP
provider_slug: amqp
slug: amqp-amqp-exchange-context
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
