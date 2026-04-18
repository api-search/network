---
description: ''
layout: schema
name: GetMetricStatisticsInput
properties_list:
- description: The namespace of the metric.
  name: Namespace
  type: string
- description: The name of the metric.
  name: MetricName
  type: string
- description: The dimensions to filter the metric.
  name: Dimensions
  type: array
- description: The time stamp that determines the first data point to return.
  name: StartTime
  type: string
- description: The time stamp that determines the last data point to return.
  name: EndTime
  type: string
- description: The granularity, in seconds, of the returned data points.
  name: Period
  type: integer
- description: The metric statistics.
  name: Statistics
  type: array
- description: The percentile statistics.
  name: ExtendedStatistics
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-get-metric-statistics-input-schema.json
slug: cloudwatch-get-metric-statistics-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: GetMetricStatisticsInput
---
