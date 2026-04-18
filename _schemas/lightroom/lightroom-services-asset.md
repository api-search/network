---
description: ''
layout: schema
name: Asset
properties_list:
- description: Unique identifier of the asset
  name: id
  type: string
- description: Resource type
  name: type
  type: string
- description: Asset subtype
  name: subtype
  type: string
- description: Asset creation timestamp
  name: created
  type: string
- description: Asset last updated timestamp
  name: updated
  type: string
- description: List of revision identifiers
  name: revision_ids
  type: array
- description: Asset payload containing metadata
  name: payload
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-services-asset-schema.json
slug: lightroom-services-asset
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: Asset
---
