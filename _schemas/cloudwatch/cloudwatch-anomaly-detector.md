---
description: An anomaly detection model associated with a particular CloudWatch metric.
layout: schema
name: AnomalyDetector
properties_list:
- description: The namespace of the metric associated with the anomaly detection model.
  name: Namespace
  type: string
- description: The name of the metric associated with the anomaly detection model.
  name: MetricName
  type: string
- description: The metric dimensions associated with the anomaly detection model.
  name: Dimensions
  type: array
- description: The statistic associated with the anomaly detection model.
  name: Stat
  type: string
- description: The current status of the anomaly detector model.
  name: StateValue
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-anomaly-detector-schema.json
slug: cloudwatch-anomaly-detector
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: AnomalyDetector
---
