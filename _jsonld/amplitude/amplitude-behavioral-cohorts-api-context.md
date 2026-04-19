---
class_count: 8
classes:
- CohortListResponse
- CohortUploadResponse
- CohortUploadRequest
- CohortRequestResponse
- Cohort
- CohortStatusResponse
- name
- description
context_file: json-ld/amplitude-behavioral-cohorts-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-behavioral-cohorts-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Behavioral Cohorts Api from Amplitude.
layout: jsonld
name: Amplitude Behavioral Cohorts Api Context
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
  name: cohorts
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: lastComputed
  type: dateTime
- container: ''
  name: archived
  type: boolean
- container: ''
  name: owner
  type: string
- container: ''
  name: appId
  type: integer
- container: ''
  name: cohortId
  type: string
- container: set
  name: ids
  type: string
- container: ''
  name: existingCohortId
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: status
  type: string
property_count: 12
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-behavioral-cohorts-api-context
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
