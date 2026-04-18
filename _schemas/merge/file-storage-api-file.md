---
description: A file object from a connected file storage platform.
layout: schema
name: File
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: remote_id
  type: string
- description: File name.
  name: name
  type: string
- description: ''
  name: file_url
  type: string
- description: ''
  name: file_thumbnail_url
  type: string
- description: File size in bytes.
  name: size
  type: integer
- description: ''
  name: mime_type
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: folder
  type: string
- description: ''
  name: drive
  type: string
- description: ''
  name: remote_was_deleted
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: modified_at
  type: string
provider_name: Merge
provider_slug: merge
schema_file: json-schema/file-storage-api-file-schema.json
slug: file-storage-api-file
tags:
- Integrations
- Platform
- Unified API
title: File
---
