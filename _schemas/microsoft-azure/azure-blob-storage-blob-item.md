---
description: A blob item in the enumeration results.
layout: schema
name: BlobItem
properties_list:
- description: The name of the blob.
  name: Name
  type: string
- description: Whether the blob is deleted.
  name: Deleted
  type: boolean
- description: The snapshot DateTime.
  name: Snapshot
  type: string
- description: The version ID of the blob.
  name: VersionId
  type: string
- description: Whether this is the current version.
  name: IsCurrentVersion
  type: boolean
- description: The blob metadata.
  name: Metadata
  type: object
- description: Blob tags.
  name: Tags
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-blob-storage-blob-item-schema.json
slug: azure-blob-storage-blob-item
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: BlobItem
---
