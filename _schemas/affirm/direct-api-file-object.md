---
description: Represents a file uploaded to Affirm's servers.
layout: schema
name: FileObject
properties_list:
- description: Unique identifier for the uploaded file.
  name: id
  type: string
- description: Original filename of the uploaded file.
  name: filename
  type: string
- description: File size in bytes.
  name: size
  type: integer
- description: MIME type of the uploaded file.
  name: content_type
  type: string
- description: Intended purpose of the file.
  name: purpose
  type: string
- description: Upload timestamp in RFC 3339 format.
  name: created
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/direct-api-file-object-schema.json
slug: direct-api-file-object
tags: []
title: FileObject
---
