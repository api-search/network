---
description: Metadata for an Adobe Stock file
layout: schema
name: StockFile
properties_list:
- description: Unique Adobe Stock content identifier
  name: id
  type: integer
- description: Title of the stock file as provided by the contributor
  name: title
  type: string
- description: Display name of the file's creator/contributor
  name: creator_name
  type: string
- description: Unique identifier of the creator on Adobe Stock
  name: creator_id
  type: integer
- description: Country of origin of the creator
  name: country_name
  type: string
- description: Original width of the file in pixels
  name: width
  type: integer
- description: Original height of the file in pixels
  name: height
  type: integer
- description: Numeric identifier for the media type (1=photo, 2=illustration, 3=vector, 4=video, 6=3D, 7=template)
  name: media_type_id
  type: integer
- description: MIME type of the stock file
  name: content_type
  type: string
- description: List of keywords describing the file content
  name: keywords
  type: array
- description: URL of the watermarked comp image for preview purposes
  name: comp_url
  type: string
- description: URL of the thumbnail image
  name: thumbnail_url
  type: string
- description: Width of the thumbnail image in pixels
  name: thumbnail_width
  type: integer
- description: Height of the thumbnail image in pixels
  name: thumbnail_height
  type: integer
- description: Licensing status of the file for the authenticated user
  name: is_licensed
  type: string
- description: Vector file subtype (svg or zip) if applicable
  name: vector_type
  type: string
- description: ''
  name: category
  type: object
- description: Total number of results matching the search query (on first item only)
  name: nb_results
  type: integer
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-stock-stock-file-schema.json
slug: adobe-creative-suite-stock-stock-file
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: StockFile
---
