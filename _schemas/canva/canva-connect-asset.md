---
description: A Canva asset (image or video)
layout: schema
name: Asset
properties_list:
- description: The asset ID
  name: id
  type: string
- description: The asset type
  name: type
  type: string
- description: The asset name
  name: name
  type: string
- description: User-facing tags for the asset
  name: tags
  type: array
- description: Unix timestamp in seconds when the asset was created
  name: created_at
  type: integer
- description: Unix timestamp in seconds when the asset was last updated
  name: updated_at
  type: integer
provider_name: Canva
provider_slug: canva
schema_file: json-schema/canva-connect-asset-schema.json
slug: canva-connect-asset
tags:
- Apps
- Automation
- Brand Management
- Collaboration
- Design
- Graphics
- Marketing
- Print
- Templates
- Visual Content
title: Asset
---
