---
description: Indicates the CloudWatch math expression that provides the time series the anomaly detector uses as input.
layout: schema
name: MetricMathAnomalyDetector
properties_list:
- description: An array of metric data query structures that enables you to create an anomaly detector based on the result of a metric math expression.
  name: MetricDataQueries
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-math-anomaly-detector-schema.json
slug: cloudwatch-metric-math-anomaly-detector
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricMathAnomalyDetector
---
