---
description: ''
layout: schema
name: ListMetricsOutput
properties_list:
- description: The metrics that match your request.
  name: Metrics
  type: array
- description: The token that marks the start of the next batch of returned results.
  name: NextToken
  type: string
- description: If you are using this operation in a monitoring account, this array contains the account IDs of the source accounts.
  name: OwningAccounts
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-list-metrics-output-schema.json
slug: cloudwatch-list-metrics-output
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: ListMetricsOutput
---
