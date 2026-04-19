---
description: Position and size of a single element within a dashboard layout
layout: schema
name: DashboardLayoutComponent
properties_list:
- description: Unique identifier
  name: id
  type: string
- description: ID of the parent layout
  name: dashboard_layout_id
  type: string
- description: ID of the dashboard element this positions
  name: dashboard_element_id
  type: string
- description: Row position in the grid
  name: row
  type: integer
- description: Column position in the grid
  name: column
  type: integer
- description: Width in grid units
  name: width
  type: integer
- description: Height in grid units
  name: height
  type: integer
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-dashboard-layout-component-schema.json
slug: looker-dashboard-layout-component
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: DashboardLayoutComponent
---
