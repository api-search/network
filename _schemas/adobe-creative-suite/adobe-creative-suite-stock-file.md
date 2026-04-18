---
description: Schema for an Adobe Stock file record as returned by the Adobe Stock Search API. Represents a stock asset such as a photo, illustration, vector, video, or template including its metadata, creator information, dimensions, thumbnail URLs, and licensing status.
layout: schema
name: Adobe Stock File
properties_list:
- description: Unique Adobe Stock content identifier assigned to this file
  name: id
  type: integer
- description: Title of the stock file as provided by the contributor
  name: title
  type: string
- description: Display name of the contributor who created and uploaded this stock file
  name: creator_name
  type: string
- description: Unique identifier of the contributor on Adobe Stock
  name: creator_id
  type: integer
- description: Country of origin of the contributor as listed in their Adobe Stock profile
  name: country_name
  type: string
- description: Original width of the stock file in pixels (for images and video)
  name: width
  type: integer
- description: Original height of the stock file in pixels (for images and video)
  name: height
  type: integer
- description: 'Numeric identifier for the media type: 1=photo, 2=illustration, 3=vector, 4=video, 6=3D, 7=template'
  name: media_type_id
  type: integer
- description: MIME type of the stock file
  name: content_type
  type: string
- description: List of keyword objects describing the content and subject matter of the file
  name: keywords
  type: array
- description: URL of the watermarked comp image for preview and design mockup purposes. The comp is a lower-resolution, watermarked version of the full file.
  name: comp_url
  type: string
- description: URL of the small thumbnail image used in search result lists
  name: thumbnail_url
  type: string
- description: Width of the thumbnail image in pixels
  name: thumbnail_width
  type: integer
- description: Height of the thumbnail image in pixels
  name: thumbnail_height
  type: integer
- description: URL of a medium-size (500px) preview image
  name: thumbnail_500_url
  type: string
- description: URL of a larger (1000px) preview image
  name: thumbnail_1000_url
  type: string
- description: Licensing status of this file for the authenticated user. Empty string if not licensed.
  name: is_licensed
  type: string
- description: Vector file subtype for vector and illustration assets. Empty string for non-vector assets.
  name: vector_type
  type: string
- description: Primary category classification of this stock file
  name: category
  type: object
- description: 'Premium content level: 0=standard, 1=premium, 2=premium+'
  name: premium_level_id
  type: integer
- description: Whether this asset is editorial use only (not for commercial purposes)
  name: is_editorial
  type: boolean
- description: Whether this asset has model or property releases on file
  name: has_releases
  type: boolean
- description: Total number of results matching the search query. Only present on the first result in a search response.
  name: nb_results
  type: integer
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-stock-file-schema.json
slug: adobe-creative-suite-stock-file
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: Adobe Stock File
---
