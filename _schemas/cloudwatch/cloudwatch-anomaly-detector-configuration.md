---
description: The configuration specifies details about how the anomaly detection model is to be trained.
layout: schema
name: AnomalyDetectorConfiguration
properties_list:
- description: An array of time ranges to exclude from use when the anomaly detection model is trained.
  name: ExcludedTimeRanges
  type: array
- description: The time zone to use for the metric.
  name: MetricTimezone
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-anomaly-detector-configuration-schema.json
slug: cloudwatch-anomaly-detector-configuration
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: AnomalyDetectorConfiguration
---
