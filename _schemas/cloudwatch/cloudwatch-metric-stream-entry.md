---
description: Contains information about a metric stream.
layout: schema
name: MetricStreamEntry
properties_list:
- description: The ARN of the metric stream.
  name: Arn
  type: string
- description: The date when the metric stream was created.
  name: CreationDate
  type: string
- description: The date when the metric stream was last updated.
  name: LastUpdateDate
  type: string
- description: The name of the metric stream.
  name: Name
  type: string
- description: The ARN of the Kinesis Data Firehose delivery stream used by this metric stream.
  name: FirehoseArn
  type: string
- description: The current state of the metric stream.
  name: State
  type: string
- description: The output format of the metric stream.
  name: OutputFormat
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-metric-stream-entry-schema.json
slug: cloudwatch-metric-stream-entry
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MetricStreamEntry
---
