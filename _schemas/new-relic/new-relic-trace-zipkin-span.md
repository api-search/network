---
description: A single span in Zipkin JSON v2 format
layout: schema
name: ZipkinSpan
properties_list:
- description: Span ID (16 hex characters)
  name: id
  type: string
- description: Trace ID (32 hex characters)
  name: traceId
  type: string
- description: Parent span ID
  name: parentId
  type: string
- description: Span name / operation name
  name: name
  type: string
- description: Span start time in microseconds since epoch
  name: timestamp
  type: integer
- description: Span duration in microseconds
  name: duration
  type: integer
- description: ''
  name: kind
  type: string
- description: ''
  name: localEndpoint
  type: object
- description: ''
  name: remoteEndpoint
  type: object
- description: ''
  name: tags
  type: object
- description: ''
  name: annotations
  type: array
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/new-relic-trace-zipkin-span-schema.json
slug: new-relic-trace-zipkin-span
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
title: ZipkinSpan
---
