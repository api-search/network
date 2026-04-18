---
description: A batch of spans with optional shared attributes
layout: schema
name: SpanBatch
properties_list:
- description: Shared attributes applied to all spans in this batch
  name: common
  type: object
- description: Array of individual span objects
  name: spans
  type: array
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/new-relic-trace-span-batch-schema.json
slug: new-relic-trace-span-batch
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
title: SpanBatch
---
