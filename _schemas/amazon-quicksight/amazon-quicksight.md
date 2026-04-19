---
description: Schema defining the structure of an Amazon QuickSight dashboard resource, including datasets, data sources, analyses, visuals, and embedding configurations for business intelligence.
layout: schema
name: Amazon QuickSight Dashboard Definition
properties_list:
- description: The unique identifier for the dashboard.
  name: DashboardId
  type: string
- description: The Amazon Resource Name of the dashboard.
  name: Arn
  type: string
- description: The display name of the dashboard.
  name: Name
  type: string
- description: ''
  name: Version
  type: object
- description: The time this dashboard was created.
  name: CreatedTime
  type: string
- description: The time this dashboard was last published.
  name: LastPublishedTime
  type: string
- description: The time this dashboard was last updated.
  name: LastUpdatedTime
  type: string
provider_name: Amazon QuickSight
provider_slug: amazon-quicksight
schema_file: json-schema/amazon-quicksight-schema.json
slug: amazon-quicksight
tags:
- Analytics
- AWS
- BI
- Business Intelligence
- Dashboards
- Machine Learning
- Reporting
- Visualization
title: Amazon QuickSight Dashboard Definition
---
