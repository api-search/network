---
description: StorageOutput from Adobe Photoshop API
layout: schema
name: StorageOutput
properties_list:
- description: Pre-signed PUT URL or Creative Cloud asset path.
  name: href
  type: string
- description: Storage type for the output file.
  name: storage
  type: string
- description: Output file format.
  name: type
  type: string
- description: Optional output width in pixels for resizing.
  name: width
  type: integer
- description: Whether to overwrite existing files.
  name: overwrite
  type: boolean
provider_name: Adobe Photoshop
provider_slug: adobe-photoshop
schema_file: json-schema/adobe-photoshop-api-storage-output-schema.json
slug: adobe-photoshop-api-storage-output
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
title: StorageOutput
---
