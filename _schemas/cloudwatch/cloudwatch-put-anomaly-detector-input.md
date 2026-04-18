---
description: ''
layout: schema
name: PutAnomalyDetectorInput
properties_list:
- description: The namespace of the metric to create the anomaly detection model for.
  name: Namespace
  type: string
- description: The name of the metric to create the anomaly detection model for.
  name: MetricName
  type: string
- description: The metric dimensions to create the anomaly detection model for.
  name: Dimensions
  type: array
- description: The statistic to use for the metric and the anomaly detection model.
  name: Stat
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-put-anomaly-detector-input-schema.json
slug: cloudwatch-put-anomaly-detector-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: PutAnomalyDetectorInput
---
