---
description: This object includes parameters that you can use to provide information to CloudWatch to help it build more accurate anomaly detection models.
layout: schema
name: MetricCharacteristics
properties_list:
- description: Set this parameter to true if values for this metric consistently include spikes that should not be considered to be anomalies.
  name: PeriodicSpikes
  type: boolean
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-characteristics-schema.json
slug: cloudwatch-metric-characteristics
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricCharacteristics
---
