---
description: ''
layout: schema
name: DeleteAnomalyDetectorInput
properties_list:
- description: The namespace associated with the anomaly detection model to delete.
  name: Namespace
  type: string
- description: The metric name associated with the anomaly detection model to delete.
  name: MetricName
  type: string
- description: The metric dimensions associated with the anomaly detection model to delete.
  name: Dimensions
  type: array
- description: The statistic associated with the anomaly detection model to delete.
  name: Stat
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-delete-anomaly-detector-input-schema.json
slug: cloudwatch-delete-anomaly-detector-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DeleteAnomalyDetectorInput
---
