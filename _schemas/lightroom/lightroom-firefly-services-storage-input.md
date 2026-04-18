---
description: Reference to an input file stored in cloud storage
layout: schema
name: StorageInput
properties_list:
- description: URL or path to the input file. For Creative Cloud, use the asset path. For external storage, use the presigned URL.
  name: href
  type: string
- description: Storage type where the input file is located
  name: storage
  type: string
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-firefly-services-storage-input-schema.json
slug: lightroom-firefly-services-storage-input
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: StorageInput
---
