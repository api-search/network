---
class_count: 2
classes:
- PinChangeRequest
- PinChangeResponse
context_file: json-ld/adyen-configuration-pin-change-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-pin-change-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Pin Change from Adyen.
layout: jsonld
name: Adyen Configuration Pin Change Context
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
  name: encryptedKey
  type: string
- container: ''
  name: encryptedPinBlock
  type: string
- container: ''
  name: paymentInstrumentId
  type: string
- container: ''
  name: token
  type: string
- container: ''
  name: status
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-pin-change-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
