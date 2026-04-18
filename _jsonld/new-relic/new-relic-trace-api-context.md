---
class_count: 6
classes:
- SpanBatch
- CommonBlock
- Span
- ZipkinSpan
- name
- AcceptedResponse
context_file: json-ld/new-relic-trace-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-ld/new-relic-trace-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for New Relic Trace Api from New Relic.
layout: jsonld
name: New Relic Trace Api Context
namespaces:
- prefix: nr
  uri: https://docs.newrelic.com/docs/schemas/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: common
  type: string
- container: set
  name: spans
  type: string
- container: ''
  name: attributes
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: trace.id
  type: string
- container: ''
  name: timestamp
  type: integer
- container: ''
  name: traceId
  type: string
- container: ''
  name: parentId
  type: string
- container: ''
  name: duration
  type: integer
- container: ''
  name: kind
  type: string
- container: ''
  name: localEndpoint
  type: reference
- container: ''
  name: remoteEndpoint
  type: reference
- container: ''
  name: tags
  type: reference
- container: set
  name: annotations
  type: string
- container: ''
  name: requestId
  type: string
property_count: 15
provider_name: New Relic
provider_slug: new-relic
slug: new-relic-trace-api-context
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
- JSON-LD
- Linked Data
- Semantic Web
---
