---
description: Specifies one range of days or times to exclude from use for training an anomaly detection model.
layout: schema
name: Range
properties_list:
- description: The start time of the range to exclude.
  name: StartTime
  type: string
- description: The end time of the range to exclude.
  name: EndTime
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-range-schema.json
slug: cloudwatch-range
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: Range
---
