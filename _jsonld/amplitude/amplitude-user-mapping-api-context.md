---
class_count: 4
classes:
- UserMapRequest
- UserMapResponse
- UserUnmapRequest
- UserMapping
context_file: json-ld/amplitude-user-mapping-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-user-mapping-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude User Mapping Api from Amplitude.
layout: jsonld
name: Amplitude User Mapping Api Context
namespaces:
- prefix: amplitude
  uri: https://amplitude.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: mapping
  type: reference
- container: ''
  name: globalUserId
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: unmap
  type: boolean
- container: ''
  name: code
  type: integer
- container: ''
  name: success
  type: boolean
property_count: 6
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-user-mapping-api-context
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
- JSON-LD
- Linked Data
- Semantic Web
---
