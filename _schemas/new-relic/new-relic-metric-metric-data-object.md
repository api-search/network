---
description: A container for a batch of metrics with optional shared attributes
layout: schema
name: MetricDataObject
properties_list:
- description: Shared attributes applied to all metrics in this data object unless overridden at the metric level
  name: common
  type: object
- description: Array of individual metric data points
  name: metrics
  type: array
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/new-relic-metric-metric-data-object-schema.json
slug: new-relic-metric-metric-data-object
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
title: MetricDataObject
---
