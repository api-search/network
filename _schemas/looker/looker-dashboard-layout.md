---
description: Layout configuration for a dashboard defining tile positions
layout: schema
name: DashboardLayout
properties_list:
- description: Unique identifier for this layout
  name: id
  type: string
- description: ID of the parent dashboard
  name: dashboard_id
  type: string
- description: Layout type
  name: type
  type: string
- description: Whether this is the active layout
  name: active
  type: boolean
- description: Width of each column in the grid
  name: column_width
  type: integer
- description: Total width of the layout
  name: width
  type: integer
- description: Positioning of elements within this layout
  name: dashboard_layout_components
  type: array
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-dashboard-layout-schema.json
slug: looker-dashboard-layout
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: DashboardLayout
---
