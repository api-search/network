---
description: ''
layout: schema
name: CatalogResponse
properties_list:
- description: Base URL for the API
  name: base
  type: string
- description: Unique identifier of the catalog
  name: id
  type: string
- description: Resource type
  name: type
  type: string
- description: Catalog creation timestamp
  name: created
  type: string
- description: Catalog last updated timestamp
  name: updated
  type: string
- description: Catalog payload data
  name: payload
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-services-catalog-response-schema.json
slug: lightroom-services-catalog-response
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: CatalogResponse
---
