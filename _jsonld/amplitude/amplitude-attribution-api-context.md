---
class_count: 3
classes:
- AttributionEvent
- AttributionResponse
- AttributionRequest
context_file: json-ld/amplitude-attribution-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-attribution-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Attribution Api from Amplitude.
layout: jsonld
name: Amplitude Attribution Api Context
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
  name: userId
  type: string
- container: ''
  name: deviceId
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: platform
  type: string
- container: ''
  name: osName
  type: string
- container: ''
  name: osVersion
  type: string
- container: ''
  name: deviceBrand
  type: string
- container: ''
  name: deviceManufacturer
  type: string
- container: ''
  name: deviceModel
  type: string
- container: ''
  name: carrier
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: adid
  type: string
- container: ''
  name: idfa
  type: string
- container: ''
  name: idfv
  type: string
- container: ''
  name: userProperties
  type: reference
- container: ''
  name: eventProperties
  type: reference
- container: ''
  name: time
  type: integer
- container: ''
  name: code
  type: integer
- container: ''
  name: eventsIngested
  type: integer
- container: ''
  name: serverUploadTime
  type: integer
- container: ''
  name: apiKey
  type: string
- container: ''
  name: event
  type: reference
property_count: 25
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-attribution-api-context
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
