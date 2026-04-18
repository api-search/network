---
description: Represents a file, folder, or other item stored in a drive.
layout: schema
name: DriveItem
properties_list:
- description: The unique identifier of the item within the drive.
  name: id
  type: string
- description: The name of the item (filename and extension).
  name: name
  type: string
- description: A user-visible description of the item.
  name: description
  type: string
- description: Size of the item in bytes.
  name: size
  type: integer
- description: URL that displays the resource in the browser.
  name: webUrl
  type: string
- description: WebDAV compatible URL for the item.
  name: webDavUrl
  type: string
- description: Date and time of item creation.
  name: createdDateTime
  type: string
- description: Date and time the item was last modified.
  name: lastModifiedDateTime
  type: string
- description: ETag for the entire item.
  name: eTag
  type: string
- description: ETag for the content of the item.
  name: cTag
  type: string
- description: ''
  name: createdBy
  type: object
- description: ''
  name: lastModifiedBy
  type: object
- description: ''
  name: parentReference
  type: object
- description: ''
  name: file
  type: object
- description: ''
  name: folder
  type: object
provider_name: Microsoft Word
provider_slug: microsoft-word
schema_file: json-schema/graph-api-drive-item-schema.json
slug: graph-api-drive-item
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
title: DriveItem
---
