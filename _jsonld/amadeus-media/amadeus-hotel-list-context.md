---
class_count: 4
classes:
- Error_404
- Error_500
- Error_400
- HotelSearchResponse
context_file: json-ld/amadeus-hotel-list-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/json-ld/amadeus-hotel-list-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Hotel List from Amadeus Media.
layout: jsonld
name: Amadeus Hotel List Context
namespaces:
- prefix: amadeus
  uri: https://amadeus.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: errors
  type: ''
- container: ''
  name: status
  type: integer
- container: ''
  name: code
  type: integer
- container: ''
  name: title
  type: string
- container: ''
  name: detail
  type: string
- container: ''
  name: source
  type: reference
- container: ''
  name: parameter
  type: string
- container: ''
  name: pointer
  type: string
- container: ''
  name: example
  type: string
- container: ''
  name: documentation
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: meta
  type: string
property_count: 12
provider_name: Amadeus Media
provider_slug: amadeus-media
slug: amadeus-hotel-list-context
tags:
- Content
- Hotels
- Images
- Media
- Travel
- JSON-LD
- Linked Data
- Semantic Web
---
