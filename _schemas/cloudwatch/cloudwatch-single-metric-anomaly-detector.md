---
description: Designates the CloudWatch metric and statistic that provides the time series the anomaly detector uses as input.
layout: schema
name: SingleMetricAnomalyDetector
properties_list:
- description: If the CloudWatch metric that provides the time series is in another account, use this to specify that account ID.
  name: AccountId
  type: string
- description: The namespace of the metric to create the anomaly detection model for.
  name: Namespace
  type: string
- description: The name of the metric to create the anomaly detection model for.
  name: MetricName
  type: string
- description: The metric dimensions to create the anomaly detection model for.
  name: Dimensions
  type: array
- description: The statistic to use for the metric and anomaly detection model.
  name: Stat
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-single-metric-anomaly-detector-schema.json
slug: cloudwatch-single-metric-anomaly-detector
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: SingleMetricAnomalyDetector
---
