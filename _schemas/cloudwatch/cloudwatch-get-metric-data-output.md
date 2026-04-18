---
description: ''
layout: schema
name: GetMetricDataOutput
properties_list:
- description: The metrics that are returned, including the metric name, namespace, and dimensions.
  name: MetricDataResults
  type: array
- description: A token that marks the next batch of returned results.
  name: NextToken
  type: string
- description: Contains a message about the operation or the results.
  name: Messages
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-get-metric-data-output-schema.json
slug: cloudwatch-get-metric-data-output
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: GetMetricDataOutput
---
