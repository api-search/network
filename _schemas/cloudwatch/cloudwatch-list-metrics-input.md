---
description: ''
layout: schema
name: ListMetricsInput
properties_list:
- description: Filters the results to only those metrics in the specified namespace.
  name: Namespace
  type: string
- description: Filters the results to only the specified metric name.
  name: MetricName
  type: string
- description: Filters the results to only those metrics that match the specified dimensions.
  name: Dimensions
  type: array
- description: The token returned by a previous call to indicate there is more data available.
  name: NextToken
  type: string
- description: To filter the results to show only metrics that have had data points published in the past three hours, specify this parameter with a value of PT3H.
  name: RecentlyActive
  type: string
- description: If you are using this operation in a monitoring account, specify true to include metrics from source accounts in the returned data.
  name: IncludeLinkedAccounts
  type: boolean
- description: When you use this operation in a monitoring account, use this field to return metrics only from one source account.
  name: OwningAccount
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-list-metrics-input-schema.json
slug: cloudwatch-list-metrics-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: ListMetricsInput
---
