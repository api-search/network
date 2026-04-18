---
class_count: 4
classes:
- Ticket
- Comment
- Project
- Attachment
context_file: json-ld/merge-ticketing-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/json-ld/merge-ticketing-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Merge Ticketing Api from Merge.
layout: jsonld
name: Merge Ticketing Api Context
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
- container: set
  name: assignees
  type: reference
- container: ''
  name: creator
  type: reference
- container: ''
  name: dueDate
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: ticketType
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: ticketUrl
  type: reference
- container: ''
  name: body
  type: string
- container: ''
  name: isPrivate
  type: boolean
- container: ''
  name: fileName
  type: string
- container: ''
  name: fileUrl
  type: reference
- container: ''
  name: contentType
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: remoteWasDeleted
  type: boolean
property_count: 20
provider_name: Merge
provider_slug: merge
slug: merge-ticketing-api-context
tags:
- Integrations
- Platform
- Unified API
- JSON-LD
- Linked Data
- Semantic Web
---
