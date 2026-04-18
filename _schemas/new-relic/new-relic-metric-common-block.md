---
description: Shared attributes applied to all metrics in this data object unless overridden at the metric level
layout: schema
name: CommonBlock
properties_list:
- description: Unix timestamp in milliseconds for all metrics in this batch
  name: timestamp
  type: integer
- description: Default measurement interval in milliseconds for count and summary metrics
  name: interval.ms
  type: integer
- description: Key-value pairs applied to all metrics in the batch. Values can be strings, numbers, or booleans.
  name: attributes
  type: object
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/new-relic-metric-common-block-schema.json
slug: new-relic-metric-common-block
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
title: CommonBlock
---
