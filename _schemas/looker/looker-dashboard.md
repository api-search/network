---
description: A dashboard is a collection of tiles arranged in a layout that visualize data from queries. Dashboards support cross-filtering, drill-down, and can be shared, embedded, or scheduled.
layout: schema
name: Dashboard
properties_list:
- description: Unique identifier. Numeric for user-defined dashboards; model::dashboard_name for LookML dashboards.
  name: id
  type: string
- description: Display title of the dashboard
  name: title
  type: string
- description: Description of the dashboard's purpose
  name: description
  type: string
- description: ID of the content metadata record
  name: content_metadata_id
  type: integer
- description: Timezone for queries on this dashboard
  name: query_timezone
  type: string
- description: ID of the space (folder) containing this dashboard
  name: space_id
  type: string
- description: ID of the folder containing this dashboard
  name: folder_id
  type: string
- description: ID of the user who created this dashboard
  name: user_id
  type: integer
- description: List of tiles (elements) on this dashboard
  name: dashboard_elements
  type: array
- description: List of filters on this dashboard
  name: dashboard_filters
  type: array
- description: Layout configurations for this dashboard
  name: dashboard_layouts
  type: array
- description: CSS background color for the dashboard
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
- description: Whether this dashboard is hidden from navigation
  name: hidden
  type: boolean
- description: Whether this dashboard is read-only (LookML dashboards are read-only)
  name: readonly
  type: boolean
- description: Auto-refresh interval (e.g. 5 minutes, 1 hour)
  name: refresh_interval
  type: string
- description: Dashboard load configuration. Controls whether tiles load concurrently or sequentially.
  name: load_configuration
  type: string
- description: Preferred viewer type for the dashboard
  name: preferred_viewer
  type: string
- description: Timestamp when the dashboard was created
  name: created_at
  type: string
- description: Timestamp when the dashboard was last updated
  name: updated_at
  type: string
- description: Timestamp when the dashboard was soft-deleted
  name: deleted_at
  type: string
- description: Whether this dashboard has been soft-deleted
  name: deleted
  type: boolean
- description: Timestamp when the dashboard was last viewed
  name: last_accessed_at
  type: string
- description: Number of times the dashboard has been viewed
  name: view_count
  type: integer
- description: Number of users who have favorited this dashboard
  name: favorite_count
  type: integer
- description: Relative URL path for this dashboard
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-dashboard-schema.json
slug: looker-dashboard
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: Dashboard
---
