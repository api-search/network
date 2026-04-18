---
description: Schema for an Adobe Lightroom cloud catalog. Each Lightroom customer has a single catalog that serves as the top-level container for all their assets, albums, and metadata.
layout: schema
name: Lightroom Catalog
properties_list:
- description: Unique identifier for the catalog
  name: id
  type: string
- description: Resource type identifier
  name: type
  type: string
- description: Server-side timestamp when the catalog was created
  name: created
  type: string
- description: Server-side timestamp when the catalog was last updated
  name: updated
  type: string
- description: Catalog metadata payload
  name: payload
  type: object
- description: ''
  name: links
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-catalog-schema.json
slug: lightroom-catalog
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: Lightroom Catalog
---
