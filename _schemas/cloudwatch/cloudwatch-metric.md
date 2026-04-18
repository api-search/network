---
description: Represents a specific metric.
layout: schema
name: Metric
properties_list:
- description: The namespace of the metric.
  name: Namespace
  type: string
- description: The name of the metric.
  name: MetricName
  type: string
- description: The dimensions for the metric.
  name: Dimensions
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-schema.json
slug: cloudwatch-metric
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: Metric
---
