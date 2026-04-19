---
class_count: 11
classes:
- Representation
- LibraryInput
- Element
- ElementList
- Links
- Library
- ElementInput
- LibraryList
- name
- created_date
- modified_date
context_file: json-ld/adobe-premiere-creative-cloud-libraries-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-premiere/refs/heads/main/json-ld/adobe-premiere-creative-cloud-libraries-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Premiere Creative Cloud Libraries from Adobe Premiere Pro.
layout: jsonld
name: Adobe Premiere Creative Cloud Libraries Context
namespaces:
- prefix: apc
  uri: https://developer.adobe.com/premiere/schema/
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
  name: type
  type: string
- container: ''
  name: content
  type: reference
- container: set
  name: representations
  type: string
- container: set
  name: elements
  type: string
- container: ''
  name: totalCount
  type: integer
- container: ''
  name: start
  type: integer
- container: ''
  name: limit
  type: integer
- container: ''
  name: self
  type: reference
- container: ''
  name: totalElements
  type: integer
- container: ''
  name: links
  type: string
- container: set
  name: libraries
  type: string
property_count: 12
provider_name: Adobe Premiere Pro
provider_slug: adobe-premiere
slug: adobe-premiere-creative-cloud-libraries-context
tags:
- Adobe
- Automation
- Creative Cloud
- Media
- Premiere Pro
- Video Editing
- Video Production
- JSON-LD
- Linked Data
- Semantic Web
---
