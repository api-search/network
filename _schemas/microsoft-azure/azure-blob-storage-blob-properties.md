---
description: Properties of a blob.
layout: schema
name: BlobProperties
properties_list:
- description: The date/time the blob was created.
  name: Creation-Time
  type: string
- description: The date/time the blob was last modified.
  name: Last-Modified
  type: string
- description: The ETag of the blob.
  name: Etag
  type: string
- description: The size of the blob in bytes.
  name: Content-Length
  type: integer
- description: The content type of the blob.
  name: Content-Type
  type: string
- description: The content encoding of the blob.
  name: Content-Encoding
  type: string
- description: The content language of the blob.
  name: Content-Language
  type: string
- description: The MD5 hash of the blob content.
  name: Content-MD5
  type: string
- description: The content disposition of the blob.
  name: Content-Disposition
  type: string
- description: The cache control of the blob.
  name: Cache-Control
  type: string
- description: The type of the blob.
  name: BlobType
  type: string
- description: The access tier of the blob.
  name: AccessTier
  type: string
- description: Whether the access tier was inferred.
  name: AccessTierInferred
  type: boolean
- description: The lease status.
  name: LeaseStatus
  type: string
- description: The lease state.
  name: LeaseState
  type: string
- description: Whether the blob data and metadata are encrypted.
  name: ServerEncrypted
  type: boolean
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-blob-storage-blob-properties-schema.json
slug: azure-blob-storage-blob-properties
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: BlobProperties
---
