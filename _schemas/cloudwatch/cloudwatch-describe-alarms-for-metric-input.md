---
description: ''
layout: schema
name: DescribeAlarmsForMetricInput
properties_list:
- description: The name of the metric.
  name: MetricName
  type: string
- description: The namespace of the metric.
  name: Namespace
  type: string
- description: The percentile statistic for the metric.
  name: ExtendedStatistic
  type: string
- description: The dimensions associated with the metric.
  name: Dimensions
  type: array
- description: The period, in seconds, over which the statistic is applied.
  name: Period
  type: integer
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-describe-alarms-for-metric-input-schema.json
slug: cloudwatch-describe-alarms-for-metric-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DescribeAlarmsForMetricInput
---
