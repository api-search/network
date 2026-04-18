---
description: Reference to the output destination in cloud storage
layout: schema
name: StorageOutput
properties_list:
- description: URL or path for the output file
  name: href
  type: string
- description: Storage type for the output
  name: storage
  type: string
- description: Output image format
  name: type
  type: string
- description: Whether to overwrite existing files
  name: overwrite
  type: boolean
- description: JPEG quality (1-12) when output type is image/jpeg
  name: quality
  type: integer
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-firefly-services-storage-output-schema.json
slug: lightroom-firefly-services-storage-output
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: StorageOutput
---
