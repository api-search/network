---
description: ''
layout: schema
name: ListDashboardsInput
properties_list:
- description: If you specify this parameter, only the dashboards with names starting with the specified string are listed.
  name: DashboardNamePrefix
  type: string
- description: The token returned by a previous call to indicate there is more data available.
  name: NextToken
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-list-dashboards-input-schema.json
slug: cloudwatch-list-dashboards-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: ListDashboardsInput
---
