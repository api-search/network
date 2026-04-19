---
description: Represents a CloudWatch dashboard
layout: schema
name: Dashboard
properties_list:
- description: The name of the dashboard
  name: dashboardName
  type: string
- description: The ARN of the dashboard
  name: dashboardArn
  type: string
- description: The time stamp of when the dashboard was last modified
  name: lastModified
  type: string
- description: The size of the dashboard in bytes
  name: size
  type: integer
provider_name: Amazon CloudWatch
provider_slug: amazon-cloudwatch
schema_file: json-schema/cloudwatch-dashboard-schema.json
slug: cloudwatch-dashboard
tags:
- AWS
- CloudWatch
- Monitoring
- Observability
- Metrics
- Logs
title: Dashboard
---
