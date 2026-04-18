---
description: Summary metric value containing statistical aggregations
layout: schema
name: SummaryValue
properties_list:
- description: The number of measurements in this summary
  name: count
  type: number
- description: The sum of all measurement values
  name: sum
  type: number
- description: The minimum measurement value
  name: min
  type: number
- description: The maximum measurement value
  name: max
  type: number
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/metric-api-summary-value-schema.json
slug: metric-api-summary-value
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
title: SummaryValue
---
