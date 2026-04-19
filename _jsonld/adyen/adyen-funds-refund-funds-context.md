---
class_count: 2
classes:
- RefundFundsTransferRequest
- RefundFundsTransferResponse
context_file: json-ld/adyen-funds-refund-funds-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-funds-refund-funds-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Funds Refund Funds from Adyen.
layout: jsonld
name: Adyen Funds Refund Funds Context
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
  name: amount
  type: string
- container: ''
  name: merchantReference
  type: string
- container: ''
  name: originalReference
  type: string
- container: set
  name: invalidFields
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-funds-refund-funds-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
