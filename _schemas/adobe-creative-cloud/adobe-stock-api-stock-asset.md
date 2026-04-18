---
description: StockAsset from Adobe API
layout: schema
name: StockAsset
properties_list:
- description: Unique asset identifier.
  name: id
  type: integer
- description: ''
  name: title
  type: string
- description: ''
  name: creator_name
  type: string
- description: ''
  name: creator_id
  type: integer
- description: Asset type (photo, illustration, vector, video, template, 3d).
  name: content_type
  type: string
- description: ''
  name: width
  type: integer
- description: ''
  name: height
  type: integer
- description: ''
  name: thumbnail_url
  type: string
- description: ''
  name: thumbnail_width
  type: integer
- description: ''
  name: thumbnail_height
  type: integer
- description: URL to the watermarked comp/preview.
  name: comp_url
  type: string
- description: ''
  name: category
  type: object
- description: ''
  name: keywords
  type: array
- description: License type if already licensed, empty string if not.
  name: is_licensed
  type: string
- description: 0 = Core, 1 = Free, 2 = Premium Collection 1, 3 = Premium Collection 2.
  name: premium_level_id
  type: integer
provider_name: Adobe Creative Cloud
provider_slug: adobe-creative-cloud
schema_file: json-schema/adobe-stock-api-stock-asset-schema.json
slug: adobe-stock-api-stock-asset
tags:
- AI/ML
- Cloud
- Creative
- Design
- Documents
- Photography
- SaaS
- Video
title: StockAsset
---
