---
description: Metadata for a file or folder in the CMS Developer File System
layout: schema
name: AssetFileMetadata
properties_list:
- description: The full path of the file in the CMS Developer File System
  name: id
  type: string
- description: The name of the file or folder
  name: name
  type: string
- description: Whether this path represents a folder (true) or file (false)
  name: folder
  type: boolean
- description: List of child files and folders (only present for folders)
  name: children
  type: array
- description: Content hash for change detection
  name: hash
  type: string
- description: Unix timestamp when the file was created
  name: createdAt
  type: integer
- description: Unix timestamp when the file was last updated
  name: updatedAt
  type: integer
- description: Unix timestamp when the file was archived (if applicable)
  name: archivedAt
  type: integer
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-source-code-asset-file-metadata-schema.json
slug: hubspot-source-code-asset-file-metadata
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: AssetFileMetadata
---
