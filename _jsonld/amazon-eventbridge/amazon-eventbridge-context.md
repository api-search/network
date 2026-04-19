---
class_count: 5
classes:
- version
- detail-type
- account
- region
- detail
context_file: json-ld/amazon-eventbridge-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-eventbridge/refs/heads/main/json-ld/amazon-eventbridge-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Eventbridge from Amazon EventBridge.
layout: jsonld
name: Amazon Eventbridge Context
namespaces:
- prefix: eventbridge
  uri: https://aws.amazon.com/eventbridge/schemas/
- prefix: aws
  uri: https://aws.amazon.com/schemas/
properties:
- container: ''
  name: id
  type: reference
- container: ''
  name: source
  type: reference
- container: ''
  name: time
  type: http://www.w3.org/2001/XMLSchema#dateTime
- container: set
  name: resources
  type: reference
- container: ''
  name: EventBus
  type: ''
- container: ''
  name: Rule
  type: ''
- container: ''
  name: Target
  type: ''
- container: ''
  name: Archive
  type: ''
- container: ''
  name: Event
  type: ''
property_count: 9
provider_name: Amazon EventBridge
provider_slug: amazon-eventbridge
slug: amazon-eventbridge-context
tags:
- Amazon Web Services
- AWS
- Event Bus
- Event-Driven
- Events
- Integration
- Serverless
- JSON-LD
- Linked Data
- Semantic Web
---
