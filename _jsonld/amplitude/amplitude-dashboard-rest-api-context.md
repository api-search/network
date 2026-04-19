---
class_count: 7
classes:
- EventListResult
- UserSearchResult
- UserActivityResult
- FunnelResult
- RetentionResult
- SegmentationResult
- name
context_file: json-ld/amplitude-dashboard-rest-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-dashboard-rest-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Dashboard Rest Api from Amplitude.
layout: jsonld
name: Amplitude Dashboard Rest Api Context
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
  name: data
  type: reference
- container: ''
  name: totals
  type: integer
- container: set
  name: matches
  type: reference
- container: ''
  name: userId
  type: string
- container: ''
  name: amplitudeId
  type: integer
- container: ''
  name: userData
  type: reference
- container: set
  name: events
  type: reference
- container: set
  name: series
  type: reference
- container: set
  name: seriesLabels
  type: string
- container: set
  name: xValues
  type: string
property_count: 10
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-dashboard-rest-api-context
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
