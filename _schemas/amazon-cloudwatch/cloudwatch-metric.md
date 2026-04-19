---
description: Represents a specific metric
layout: schema
name: Metric
properties_list:
- description: The namespace of the metric
  name: namespace
  type: string
- description: The name of the metric
  name: metricName
  type: string
- description: The dimensions for the metric
  name: dimensions
  type: array
provider_name: Amazon CloudWatch
provider_slug: amazon-cloudwatch
schema_file: json-schema/cloudwatch-metric-schema.json
slug: cloudwatch-metric
tags:
- AWS
- CloudWatch
- Monitoring
- Observability
- Metrics
- Logs
title: Metric
---
