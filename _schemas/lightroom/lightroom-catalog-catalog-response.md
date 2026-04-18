---
description: ''
layout: schema
name: CatalogResponse
properties_list:
- description: Base URL for the API
  name: base
  type: string
- description: Unique catalog identifier
  name: id
  type: string
- description: Resource type
  name: type
  type: string
- description: Server-side creation timestamp
  name: created
  type: string
- description: Server-side last updated timestamp
  name: updated
  type: string
- description: Catalog metadata
  name: payload
  type: object
- description: HATEOAS links to related resources
  name: links
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-catalog-catalog-response-schema.json
slug: lightroom-catalog-catalog-response
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: CatalogResponse
---
