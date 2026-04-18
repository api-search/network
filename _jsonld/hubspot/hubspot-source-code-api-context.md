---
class_count: 8
classes:
- AssetFileMetadata
- FileUploadRequest
- FileExtractRequest
- TaskLocator
- ActionResponse
- ValidationResult
- ValidationError
- ValidationWarning
context_file: json-ld/hubspot-source-code-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-source-code-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Source Code Api from HubSpot.
layout: jsonld
name: Hubspot Source Code Api Context
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
  name: name
  type: ''
- container: ''
  name: folder
  type: boolean
- container: set
  name: children
  type: string
- container: ''
  name: hash
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: updatedAt
  type: string
- container: ''
  name: archivedAt
  type: string
- container: ''
  name: file
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: links
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: requestedAt
  type: dateTime
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: valid
  type: boolean
- container: set
  name: errors
  type: reference
- container: set
  name: warnings
  type: reference
- container: ''
  name: message
  type: string
- container: ''
  name: line
  type: integer
- container: ''
  name: column
  type: integer
- container: ''
  name: category
  type: string
- container: ''
  name: suggestion
  type: string
property_count: 23
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-source-code-api-context
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
