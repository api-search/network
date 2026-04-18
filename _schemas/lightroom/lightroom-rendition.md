---
description: Schema for an Adobe Lightroom asset rendition. Renditions are server-generated preview images derived from the master file with current develop settings applied. Available in multiple sizes from small thumbnails to full-resolution exports.
layout: schema
name: Lightroom Rendition
properties_list:
- description: Resource type identifier
  name: type
  type: string
- description: Size classification of the rendition. thumbnail2x is a small thumbnail, numeric values indicate the longest edge in pixels, and fullsize is the maximum available resolution.
  name: rendition_type
  type: string
- description: Unique identifier of the source asset
  name: asset_id
  type: string
- description: Unique identifier of the catalog containing the source asset
  name: catalog_id
  type: string
- description: Width of the rendition in pixels
  name: width
  type: integer
- description: Height of the rendition in pixels
  name: height
  type: integer
- description: MIME type of the rendition image
  name: contentType
  type: string
- description: Size of the rendition file in bytes
  name: contentLength
  type: integer
- description: Timestamp when the rendition was generated
  name: created
  type: string
- description: Timestamp when the rendition was last regenerated
  name: updated
  type: string
- description: ''
  name: links
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-rendition-schema.json
slug: lightroom-rendition
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: Lightroom Rendition
---
