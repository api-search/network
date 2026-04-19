---
class_count: 7
classes:
- Credit Balance
- Diagnose Request
- Diagnosis Result
- Diagnosis
- Crop
- Supported Crops Response
- Error Response
context_file: json-ld/agrio-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agrio/refs/heads/main/json-ld/agrio-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agrio from agrio.
layout: jsonld
name: Agrio Context
namespaces:
- prefix: agrio
  uri: https://agrio.app/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: balance
  type: integer
- container: ''
  name: currency
  type: string
- container: ''
  name: accountId
  type: string
- container: ''
  name: cropId
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: confidence
  type: double
- container: ''
  name: commonName
  type: string
- container: ''
  name: scientificName
  type: string
- container: ''
  name: crop
  type: string
- container: ''
  name: cropConfidence
  type: string
- container: set
  name: idArray
  type: string
- container: set
  name: crops
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: status
  type: integer
property_count: 16
provider_name: agrio
provider_slug: agrio
slug: agrio-context
tags:
- Agriculture
- Plant Disease
- Pest Detection
- AI
- Crop Advisory
- JSON-LD
- Linked Data
- Semantic Web
---
