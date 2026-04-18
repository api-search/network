---
description: The default aggregation setting for the metric.
layout: schema
name: MetricDefaultAggregation
properties_list:
- description: The aggregation type to apply when no aggregation is specified in the query. For example, avg, sum, or max.
  name: type
  type: string
- description: The parameter for the aggregation type, used for percentile aggregation to specify the percentile value (e.g., 95).
  name: parameter
  type: number
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-metrics-v2-metric-default-aggregation-schema.json
slug: dynatrace-metrics-v2-metric-default-aggregation
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: MetricDefaultAggregation
---
