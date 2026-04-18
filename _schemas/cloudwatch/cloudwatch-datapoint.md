---
description: Encapsulates the statistical data that CloudWatch computes from metric data.
layout: schema
name: Datapoint
properties_list:
- description: The time stamp used for the data point.
  name: Timestamp
  type: string
- description: The number of metric values that contributed to the aggregate value of this data point.
  name: SampleCount
  type: number
- description: The average of the metric values that correspond to the data point.
  name: Average
  type: number
- description: The sum of the metric values for the data point.
  name: Sum
  type: number
- description: The minimum metric value for the data point.
  name: Minimum
  type: number
- description: The maximum metric value for the data point.
  name: Maximum
  type: number
- description: The percentile statistic for the data point.
  name: ExtendedStatistics
  type: object
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-datapoint-schema.json
slug: cloudwatch-datapoint
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: Datapoint
---
