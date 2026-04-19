---
class_count: 3
classes:
- UserProfileResponse
- UserData
- Recommendation
context_file: json-ld/amplitude-user-profile-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-user-profile-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude User Profile Api from Amplitude.
layout: jsonld
name: Amplitude User Profile Api Context
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
  name: userData
  type: reference
- container: ''
  name: userId
  type: string
- container: ''
  name: userProperties
  type: reference
- container: ''
  name: computedProperties
  type: reference
- container: set
  name: cohortIds
  type: string
- container: set
  name: recommendations
  type: reference
- container: ''
  name: amplitudeId
  type: integer
- container: ''
  name: recId
  type: string
- container: set
  name: childIds
  type: string
- container: ''
  name: isControl
  type: boolean
- container: ''
  name: recommendationType
  type: string
- container: ''
  name: title
  type: string
property_count: 12
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-user-profile-api-context
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
