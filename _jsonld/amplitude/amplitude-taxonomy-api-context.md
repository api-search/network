---
class_count: 11
classes:
- EventProperty
- EventPropertyListResponse
- CategoryListResponse
- SuccessResponse
- EventType
- EventTypeListResponse
- Category
- UserPropertyListResponse
- UserProperty
- description
- name
context_file: json-ld/amplitude-taxonomy-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-taxonomy-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Taxonomy Api from Amplitude.
layout: jsonld
name: Amplitude Taxonomy Api Context
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
  name: eventProperty
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: isRequired
  type: boolean
- container: set
  name: data
  type: reference
- container: ''
  name: id
  type: integer
- container: ''
  name: success
  type: boolean
- container: ''
  name: category
  type: string
- container: ''
  name: userProperty
  type: string
property_count: 9
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-taxonomy-api-context
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
