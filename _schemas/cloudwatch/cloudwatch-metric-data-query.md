---
description: This structure is used in both GetMetricData and PutMetricAlarm. The supported use of this structure is different for those two operations.
layout: schema
name: MetricDataQuery
properties_list:
- description: A short name used to tie this object to the results in the response.
  name: Id
  type: string
- description: This field can contain a Metrics Insights query, or a metric math expression.
  name: Expression
  type: string
- description: A human-readable label for this metric or expression.
  name: Label
  type: string
- description: When used in GetMetricData, this option indicates whether to return the timestamps and raw data values of this metric.
  name: ReturnData
  type: boolean
- description: The granularity, in seconds, of the returned data points.
  name: Period
  type: integer
- description: The ID of the account where the metrics are located.
  name: AccountId
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-data-query-schema.json
slug: cloudwatch-metric-data-query
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricDataQuery
---
