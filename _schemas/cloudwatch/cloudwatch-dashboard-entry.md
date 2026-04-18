---
description: Represents a specific dashboard.
layout: schema
name: DashboardEntry
properties_list:
- description: The name of the dashboard.
  name: DashboardName
  type: string
- description: The Amazon Resource Name (ARN) of the dashboard.
  name: DashboardArn
  type: string
- description: The time stamp of when the dashboard was last modified.
  name: LastModified
  type: string
- description: The size of the dashboard, in bytes.
  name: Size
  type: integer
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-dashboard-entry-schema.json
slug: cloudwatch-dashboard-entry
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DashboardEntry
---
