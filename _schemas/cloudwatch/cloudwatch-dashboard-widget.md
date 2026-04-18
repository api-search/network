---
description: A widget in a CloudWatch dashboard.
layout: schema
name: DashboardWidget
properties_list:
- description: The type of the widget.
  name: type
  type: string
- description: The horizontal position of the widget on the dashboard grid.
  name: x
  type: integer
- description: The vertical position of the widget on the dashboard grid.
  name: y
  type: integer
- description: The width of the widget in grid units.
  name: width
  type: integer
- description: The height of the widget in grid units.
  name: height
  type: integer
- description: The properties for the widget, which vary depending on the widget type.
  name: properties
  type: object
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-dashboard-widget-schema.json
slug: cloudwatch-dashboard-widget
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DashboardWidget
---
