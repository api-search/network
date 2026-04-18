---
description: Schema for an Adobe Lightroom asset. Assets represent individual photos or videos stored in a customer's Lightroom cloud catalog. Each asset has metadata including capture date, import source, location, and develop settings.
layout: schema
name: Lightroom Asset
properties_list:
- description: Unique identifier for the asset (UUID format)
  name: id
  type: string
- description: Resource type identifier
  name: type
  type: string
- description: Asset media type
  name: subtype
  type: string
- description: Server-side timestamp when the asset was created
  name: created
  type: string
- description: Server-side timestamp when the asset was last updated
  name: updated
  type: string
- description: List of revision identifiers tracking edit history
  name: revision_ids
  type: array
- description: Asset metadata payload
  name: payload
  type: object
- description: ''
  name: links
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-asset-schema.json
slug: lightroom-asset
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: Lightroom Asset
---
