---
description: Schema for an Adobe Lightroom album. Albums organize assets into user-defined collections within a catalog. Albums can be regular collections, collection sets (folders containing other albums), or projects.
layout: schema
name: Lightroom Album
properties_list:
- description: Unique identifier for the album (UUID format)
  name: id
  type: string
- description: Resource type identifier
  name: type
  type: string
- description: Album subtype determining its organizational role
  name: subtype
  type: string
- description: Server-side timestamp when the album was created
  name: created
  type: string
- description: Server-side timestamp when the album was last updated
  name: updated
  type: string
- description: Album metadata payload
  name: payload
  type: object
- description: ''
  name: links
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-album-schema.json
slug: lightroom-album
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: Lightroom Album
---
