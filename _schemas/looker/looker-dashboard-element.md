---
description: A single tile on a dashboard. Each element can contain a query, a reference to a Look, a merge query, or text/markdown content.
layout: schema
name: DashboardElement
properties_list:
- description: Unique identifier for this element
  name: id
  type: string
- description: ID of the parent dashboard
  name: dashboard_id
  type: string
- description: ID of a Look to display in this tile
  name: look_id
  type: integer
- description: ID of a query to run in this tile
  name: query_id
  type: integer
- description: Element type
  name: type
  type: string
- description: Display title for this tile
  name: title
  type: string
- description: Whether the title is hidden
  name: title_hidden
  type: boolean
- description: Subtitle text displayed below the title
  name: subtitle_text
  type: string
- description: Body text for text-type elements
  name: body_text
  type: string
- description: Note text displayed on the tile
  name: note_text
  type: string
- description: How the note is displayed (above, below, hover)
  name: note_display
  type: string
- description: Note display state
  name: note_state
  type: string
- description: Result maker configuration for merged queries
  name: result_maker
  type: object
- description: Rich content JSON for advanced text elements
  name: rich_content_json
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-dashboard-element-schema.json
slug: looker-dashboard-element
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: DashboardElement
---
