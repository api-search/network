---
description: A message returned by the GetMetricData API.
layout: schema
name: MessageData
properties_list:
- description: The error code or status code associated with the message.
  name: Code
  type: string
- description: The message text.
  name: Value
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-message-data-schema.json
slug: cloudwatch-message-data
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: MessageData
---
