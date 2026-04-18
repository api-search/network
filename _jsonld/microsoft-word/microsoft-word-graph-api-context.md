---
class_count: 11
classes:
- DriveItem
- Permission
- IdentitySet
- ItemReference
- FileFacet
- FolderFacet
- DriveItemVersion
- ThumbnailSet
- UploadSession
- name
- description
context_file: json-ld/microsoft-word-graph-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/json-ld/microsoft-word-graph-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Microsoft Word Graph Api from Microsoft Word.
layout: jsonld
name: Microsoft Word Graph Api Context
namespaces:
- prefix: msword
  uri: https://developer.microsoft.com/schema/word/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: webUrl
  type: reference
- container: ''
  name: webDavUrl
  type: reference
- container: ''
  name: createdDateTime
  type: dateTime
- container: ''
  name: lastModifiedDateTime
  type: dateTime
- container: ''
  name: size
  type: integer
- container: ''
  name: eTag
  type: string
- container: ''
  name: cTag
  type: string
- container: ''
  name: mimeType
  type: string
- container: ''
  name: childCount
  type: integer
- container: set
  name: roles
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: driveId
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: scope
  type: string
- container: ''
  name: uploadUrl
  type: reference
- container: ''
  name: expirationDateTime
  type: dateTime
property_count: 16
provider_name: Microsoft Word
provider_slug: microsoft-word
slug: microsoft-word-graph-api-context
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
- JSON-LD
- Linked Data
- Semantic Web
---
