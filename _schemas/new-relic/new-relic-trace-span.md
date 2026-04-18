---
description: A single distributed trace span in New Relic format
layout: schema
name: Span
properties_list:
- description: Unique identifier for this span (16 hex characters)
  name: id
  type: string
- description: Trace ID that groups all spans in a distributed trace
  name: trace.id
  type: string
- description: Unix epoch timestamp in milliseconds when the span started
  name: timestamp
  type: integer
- description: Span attributes
  name: attributes
  type: object
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/new-relic-trace-span-schema.json
slug: new-relic-trace-span
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
title: Span
---
