---
description: ''
layout: schema
name: GetDashboardOutput
properties_list:
- description: The Amazon Resource Name (ARN) of the dashboard.
  name: DashboardArn
  type: string
- description: The detailed information about the dashboard, including what widgets are included and their location.
  name: DashboardBody
  type: string
- description: The name of the dashboard.
  name: DashboardName
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-get-dashboard-output-schema.json
slug: cloudwatch-get-dashboard-output
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: GetDashboardOutput
---
