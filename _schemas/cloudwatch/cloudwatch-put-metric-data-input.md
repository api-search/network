---
description: ''
layout: schema
name: PutMetricDataInput
properties_list:
- description: The namespace for the metric data. To avoid conflicts with AWS service namespaces, you should not specify a namespace that begins with AWS/.
  name: Namespace
  type: string
- description: The data for the metric. The array can include no more than 1000 metrics per call.
  name: MetricData
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-put-metric-data-input-schema.json
slug: cloudwatch-put-metric-data-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: PutMetricDataInput
---
