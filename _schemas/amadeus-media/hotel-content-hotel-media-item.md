---
description: A detailed media item with dimensions and format information.
layout: schema
name: HotelMediaItem
properties_list:
- description: Unique identifier for the media item.
  name: id
  type: string
- description: Media category type.
  name: category
  type: string
- description: URL of the full-size image.
  name: uri
  type: string
- description: URL of the thumbnail image.
  name: thumbnailUri
  type: string
- description: Image caption or alt text.
  name: caption
  type: string
- description: Image width in pixels.
  name: width
  type: integer
- description: Image height in pixels.
  name: height
  type: integer
- description: Image format.
  name: format
  type: string
- description: Indicates whether this is the primary/featured image for this category.
  name: isPrimary
  type: boolean
provider_name: Amadeus Media
provider_slug: amadeus-media
schema_file: json-schema/hotel-content-hotel-media-item-schema.json
slug: hotel-content-hotel-media-item
tags:
- Content
- Hotels
- Images
- Media
- Travel
title: HotelMediaItem
---
