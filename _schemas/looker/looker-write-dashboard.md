---
description: Writable fields for creating or updating a dashboard
layout: schema
name: WriteDashboard
properties_list:
- description: Display title
  name: title
  type: string
- description: Description of the dashboard
  name: description
  type: string
- description: Space (folder) ID
  name: space_id
  type: string
- description: Folder ID
  name: folder_id
  type: string
- description: Timezone for queries
  name: query_timezone
  type: string
- description: CSS background color
  name: background_color
  type: string
- description: Default text color for text tiles
  name: text_tile_text_color
  type: string
- description: Default background color for tiles
  name: tile_background_color
  type: string
- description: Default text color for tiles
  name: tile_text_color
  type: string
- description: Whether the dashboard is hidden
  name: hidden
  type: boolean
- description: Auto-refresh interval
  name: refresh_interval
  type: string
- description: Tile load configuration
  name: load_configuration
  type: string
- description: Preferred viewer type
  name: preferred_viewer
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-write-dashboard-schema.json
slug: looker-write-dashboard
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: WriteDashboard
---
