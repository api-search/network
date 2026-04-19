---
description: ''
layout: schema
name: Photo
properties_list:
- description: The unique identifier of the photo.
  name: id
  type: string
- description: The URL where the photo is hosted.
  name: url
  type: string
- description: A caption describing the photo.
  name: caption
  type: string
- description: The display position of the photo in the listing gallery.
  name: sort_order
  type: integer
- description: The width of the photo in pixels.
  name: width
  type: integer
- description: The height of the photo in pixels.
  name: height
  type: integer
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-photo-schema.json
slug: airbnb-photo
tags: []
title: Photo
---
