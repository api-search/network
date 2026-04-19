---
class_count: 6
classes:
- UpdateAnnotationRequest
- CreateAnnotationRequest
- AnnotationListResponse
- Annotation
- createdAt
- updatedAt
context_file: json-ld/amplitude-chart-annotations-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-chart-annotations-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Chart Annotations Api from Amplitude.
layout: jsonld
name: Amplitude Chart Annotations Api Context
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
  name: label
  type: string
- container: ''
  name: date
  type: date
- container: ''
  name: endDate
  type: date
- container: ''
  name: details
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: chartId
  type: integer
- container: set
  name: data
  type: reference
- container: ''
  name: id
  type: integer
property_count: 8
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-chart-annotations-api-context
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
