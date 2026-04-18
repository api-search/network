---
description: ''
layout: schema
name: AlbumPayload
properties_list:
- description: Display name of the album
  name: name
  type: string
- description: When the user created the album
  name: userCreated
  type: string
- description: When the user last modified the album
  name: userUpdated
  type: string
- description: Cover asset for the album
  name: cover
  type: object
- description: Parent album reference for nested albums
  name: parent
  type: object
provider_name: Adobe Lightroom
provider_slug: lightroom
schema_file: json-schema/lightroom-albums-album-payload-schema.json
slug: lightroom-albums-album-payload
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
title: AlbumPayload
---
