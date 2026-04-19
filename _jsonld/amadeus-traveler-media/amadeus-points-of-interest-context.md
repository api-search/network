---
class_count: 9
classes:
- GeoCode
- Links
- Error_500
- Error_404
- Location
- Issue
- Collection_Meta
- Error_400
- name
context_file: json-ld/amadeus-points-of-interest-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/json-ld/amadeus-points-of-interest-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Points Of Interest from Amadeus Traveler Media.
layout: jsonld
name: Amadeus Points Of Interest Context
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
- container: ''
  name: latitude
  type: decimal
- container: ''
  name: longitude
  type: decimal
- container: ''
  name: href
  type: reference
- container: set
  name: methods
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: self
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: subType
  type: string
- container: ''
  name: geoCode
  type: string
- container: ''
  name: category
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: rank
  type: string
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
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: links
  type: string
property_count: 20
provider_name: Amadeus Traveler Media
provider_slug: amadeus-traveler-media
slug: amadeus-points-of-interest-context
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
- JSON-LD
- Linked Data
- Semantic Web
---
