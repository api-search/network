---
class_count: 2
classes:
- KafkaMessage
- KafkaTopic
context_file: json-ld/aklivity-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/json-ld/aklivity-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aklivity from Aklivity.
layout: jsonld
name: Aklivity Context
namespaces:
- prefix: aklivity
  uri: https://www.aklivity.io/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: kafka
  uri: https://kafka.apache.org/schema/
properties:
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: topic
  type: string
- container: ''
  name: partition
  type: integer
- container: ''
  name: offset
  type: integer
- container: ''
  name: timestamp
  type: dateTime
- container: set
  name: headers
  type: ''
property_count: 7
provider_name: Aklivity
provider_slug: aklivity
slug: aklivity-context
tags:
- API Gateway
- Apache Kafka
- Event-Driven
- IoT
- Kafka Proxy
- Multi-Protocol
- Real-Time
- JSON-LD
- Linked Data
- Semantic Web
---
