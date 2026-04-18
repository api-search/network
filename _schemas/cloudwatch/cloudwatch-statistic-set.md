---
description: Represents a set of statistics that describes a specific metric.
layout: schema
name: StatisticSet
properties_list:
- description: The number of samples used for the statistic set.
  name: SampleCount
  type: number
- description: The sum of values for the sample set.
  name: Sum
  type: number
- description: The minimum value of the sample set.
  name: Minimum
  type: number
- description: The maximum value of the sample set.
  name: Maximum
  type: number
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-statistic-set-schema.json
slug: cloudwatch-statistic-set
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: StatisticSet
---
