---
class_count: 1
classes:
- PaymentResult
context_file: json-ld/adyen-payments-payment-result-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payments-payment-result-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payments Payment Result from Adyen.
layout: jsonld
name: Adyen Payments Payment Result Context
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
  name: additionalData
  type: reference
- container: ''
  name: authCode
  type: string
- container: ''
  name: dccAmount
  type: string
- container: ''
  name: dccSignature
  type: string
- container: ''
  name: fraudResult
  type: string
- container: ''
  name: issuerUrl
  type: string
- container: ''
  name: md
  type: string
- container: ''
  name: paRequest
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: refusalReason
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-payments-payment-result-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
