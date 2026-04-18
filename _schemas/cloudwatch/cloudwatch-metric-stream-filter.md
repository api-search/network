---
description: Contains the configuration for a metric stream filter.
layout: schema
name: MetricStreamFilter
properties_list:
- description: The name of the metric namespace in the filter.
  name: Namespace
  type: string
- description: The names of the metrics to either include or exclude from the metric stream.
  name: MetricNames
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-stream-filter-schema.json
slug: cloudwatch-metric-stream-filter
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricStreamFilter
---
