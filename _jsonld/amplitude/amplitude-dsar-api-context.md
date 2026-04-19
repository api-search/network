---
class_count: 6
classes:
- DsarStatusResponse
- DeletionRequest
- DeletionListResponse
- DsarResponse
- DeletionResponse
- DsarRequest
context_file: json-ld/amplitude-dsar-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-dsar-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Dsar Api from Amplitude.
layout: jsonld
name: Amplitude Dsar Api Context
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
- container: ''
  name: requestId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: downloadUrl
  type: reference
- container: set
  name: amplitudeIds
  type: string
- container: set
  name: userIds
  type: string
- container: ''
  name: requester
  type: string
- container: set
  name: deletions
  type: reference
- container: ''
  name: day
  type: date
property_count: 8
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-dsar-api-context
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
