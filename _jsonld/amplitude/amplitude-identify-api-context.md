---
class_count: 5
classes:
- UserPropertyOperations
- Identification
- IdentifyResponse
- IdentifyRequestForm
- IdentifyRequestBody
context_file: json-ld/amplitude-identify-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-identify-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Identify Api from Amplitude.
layout: jsonld
name: Amplitude Identify Api Context
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
  name: $set
  type: reference
- container: ''
  name: $setOnce
  type: reference
- container: ''
  name: $add
  type: reference
- container: ''
  name: $append
  type: reference
- container: ''
  name: $prepend
  type: reference
- container: ''
  name: $unset
  type: reference
- container: ''
  name: $remove
  type: reference
- container: ''
  name: userId
  type: string
- container: ''
  name: deviceId
  type: string
- container: ''
  name: userProperties
  type: string
- container: ''
  name: code
  type: integer
- container: ''
  name: serverUploadTime
  type: integer
- container: ''
  name: eventsIngested
  type: integer
- container: ''
  name: apiKey
  type: string
- container: set
  name: identification
  type: reference
property_count: 15
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-identify-api-context
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
