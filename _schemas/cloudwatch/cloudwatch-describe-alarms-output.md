---
description: ''
layout: schema
name: DescribeAlarmsOutput
properties_list:
- description: The information about any metric alarms returned by the operation.
  name: MetricAlarms
  type: array
- description: The information about any composite alarms returned by the operation.
  name: CompositeAlarms
  type: array
- description: The token that marks the start of the next batch of returned results.
  name: NextToken
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-describe-alarms-output-schema.json
slug: cloudwatch-describe-alarms-output
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DescribeAlarmsOutput
---
