---
class_count: 2
classes:
- SubjectErasureByPspReferenceRequest
- SubjectErasureResponse
context_file: json-ld/adyen-data-protection-subject-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-data-protection-subject-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Data Protection Subject from Adyen.
layout: jsonld
name: Adyen Data Protection Subject Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: forceErasure
  type: boolean
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: result
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-data-protection-subject-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
