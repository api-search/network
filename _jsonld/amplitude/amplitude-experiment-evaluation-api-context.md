---
class_count: 4
classes:
- EvaluationResponse
- EvaluationRequest
- Variant
- FlagConfiguration
context_file: json-ld/amplitude-experiment-evaluation-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-experiment-evaluation-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Experiment Evaluation Api from Amplitude.
layout: jsonld
name: Amplitude Experiment Evaluation Api Context
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
  name: userProperties
  type: reference
- container: ''
  name: groups
  type: reference
- container: ''
  name: groupProperties
  type: reference
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: payload
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: experimentKey
  type: string
- container: ''
  name: flagType
  type: string
- container: ''
  name: flagVersion
  type: integer
- container: ''
  name: default
  type: boolean
- container: ''
  name: deployed
  type: boolean
- container: ''
  name: evaluationMode
  type: string
- container: set
  name: segments
  type: reference
- container: set
  name: conditions
  type: reference
- container: ''
  name: variant
  type: string
- container: ''
  name: variants
  type: reference
property_count: 19
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-experiment-evaluation-api-context
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
