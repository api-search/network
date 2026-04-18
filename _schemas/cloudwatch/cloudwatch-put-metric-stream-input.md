---
description: ''
layout: schema
name: PutMetricStreamInput
properties_list:
- description: The name of the metric stream.
  name: Name
  type: string
- description: If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.
  name: IncludeFilters
  type: array
- description: If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.
  name: ExcludeFilters
  type: array
- description: The ARN of the Amazon Kinesis Data Firehose delivery stream to use for this metric stream.
  name: FirehoseArn
  type: string
- description: The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Data Firehose resources.
  name: RoleArn
  type: string
- description: The output format for the stream.
  name: OutputFormat
  type: string
- description: A list of key-value pairs to associate with the metric stream.
  name: Tags
  type: array
- description: If you are creating a metric stream in a monitoring account, specify true to include metrics from source accounts.
  name: IncludeLinkedAccountsMetrics
  type: boolean
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-put-metric-stream-input-schema.json
slug: cloudwatch-put-metric-stream-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: PutMetricStreamInput
---
