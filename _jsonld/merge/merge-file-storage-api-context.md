---
class_count: 5
classes:
- File
- Folder
- Drive
- FSGroup
- FSUser
context_file: json-ld/merge-file-storage-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/json-ld/merge-file-storage-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Merge File Storage Api from Merge.
layout: jsonld
name: Merge File Storage Api Context
namespaces:
- prefix: merge
  uri: https://api.merge.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: fileUrl
  type: reference
- container: ''
  name: fileThumbnailUrl
  type: reference
- container: ''
  name: size
  type: integer
- container: ''
  name: mimeType
  type: string
- container: ''
  name: folder
  type: reference
- container: ''
  name: drive
  type: reference
- container: ''
  name: folderUrl
  type: reference
- container: ''
  name: parentFolder
  type: reference
- container: ''
  name: emailAddress
  type: string
- container: ''
  name: isMe
  type: boolean
- container: set
  name: users
  type: reference
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: remoteWasDeleted
  type: boolean
property_count: 17
provider_name: Merge
provider_slug: merge
slug: merge-file-storage-api-context
tags:
- Integrations
- Platform
- Unified API
- JSON-LD
- Linked Data
- Semantic Web
---
