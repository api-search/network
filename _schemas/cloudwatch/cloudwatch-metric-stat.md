---
description: This structure defines the metric to be returned, along with the statistics, period, and units.
layout: schema
name: MetricStat
properties_list:
- description: The granularity, in seconds, of the returned data points.
  name: Period
  type: integer
- description: The statistic to return. It can include any CloudWatch statistic or extended statistic.
  name: Stat
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-stat-schema.json
slug: cloudwatch-metric-stat
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricStat
---
