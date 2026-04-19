---
class_count: 2
classes:
- RevealPinRequest
- RevealPinResponse
context_file: json-ld/adyen-configuration-reveal-pin-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-reveal-pin-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Reveal Pin from Adyen.
layout: jsonld
name: Adyen Configuration Reveal Pin Context
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
  name: paymentInstrumentId
  type: string
- container: ''
  name: encryptedPinBlock
  type: string
- container: ''
  name: token
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-reveal-pin-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
