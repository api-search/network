---
class_count: 6
classes:
- Note
- NoteCollectionResponse
- NoteSearchResponse
- NoteCreateRequest
- NoteUpdateRequest
- NoteSearchRequest
context_file: json-ld/hubspot-engagement-notes-note-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-engagement-notes-note-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Engagement Notes Note from HubSpot.
layout: jsonld
name: Hubspot Engagement Notes Note Context
namespaces:
- prefix: hubspot
  uri: https://developers.hubspot.com/schema/
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
  name: properties
  type: reference
- container: ''
  name: propertiesWithHistory
  type: reference
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: archived
  type: boolean
- container: ''
  name: archivedAt
  type: dateTime
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: total
  type: integer
- container: set
  name: associations
  type: reference
- container: set
  name: filterGroups
  type: reference
- container: set
  name: sorts
  type: reference
- container: ''
  name: query
  type: string
- container: ''
  name: limit
  type: integer
- container: ''
  name: after
  type: string
property_count: 16
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-engagement-notes-note-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
