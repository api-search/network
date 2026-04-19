---
description: A Look is a saved query with a visualization. Looks can be shared, embedded, scheduled for delivery, and added to dashboards as tiles.
layout: schema
name: Look
properties_list:
- description: Unique numeric identifier for this Look
  name: id
  type: integer
- description: Display title of the Look
  name: title
  type: string
- description: Description of the Look's purpose
  name: description
  type: string
- description: ID of the content metadata record
  name: content_metadata_id
  type: integer
- description: ID of the query associated with this Look
  name: query_id
  type: integer
- description: ID of the space (folder) containing this Look
  name: space_id
  type: string
- description: ID of the folder containing this Look
  name: folder_id
  type: string
- description: ID of the user who created this Look
  name: user_id
  type: integer
- description: Whether this Look is publicly accessible
  name: public
  type: boolean
- description: Whether the query runs automatically when the Look is loaded
  name: is_run_on_load
  type: boolean
- description: Timestamp when the Look was created
  name: created_at
  type: string
- description: Timestamp when the Look was last updated
  name: updated_at
  type: string
- description: Timestamp when the Look was soft-deleted
  name: deleted_at
  type: string
- description: Whether this Look has been soft-deleted
  name: deleted
  type: boolean
- description: Timestamp when the Look was last viewed
  name: last_accessed_at
  type: string
- description: Number of times the Look has been viewed
  name: view_count
  type: integer
- description: Number of users who have favorited this Look
  name: favorite_count
  type: integer
- description: Relative URL path for this Look
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-look-schema.json
slug: looker-look
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: Look
---
