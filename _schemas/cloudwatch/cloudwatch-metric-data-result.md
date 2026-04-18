---
description: A GetMetricData call returns an array of MetricDataResult structures.
layout: schema
name: MetricDataResult
properties_list:
- description: The short name you specified to represent this metric.
  name: Id
  type: string
- description: The human-readable label associated with the data.
  name: Label
  type: string
- description: The timestamps for the data points, formatted in Unix epoch time.
  name: Timestamps
  type: array
- description: The data points for the metric corresponding to Timestamps.
  name: Values
  type: array
- description: The status of the returned data.
  name: StatusCode
  type: string
- description: A list of messages with additional information about the data returned.
  name: Messages
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-data-result-schema.json
slug: cloudwatch-metric-data-result
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricDataResult
---
