---
class_count: 2
classes:
- TransferFundsRequest
- TransferFundsResponse
context_file: json-ld/adyen-funds-transfer-funds-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-funds-transfer-funds-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Funds Transfer Funds from Adyen.
layout: jsonld
name: Adyen Funds Transfer Funds Context
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
  name: destinationAccountCode
  type: string
- container: ''
  name: merchantReference
  type: string
- container: ''
  name: sourceAccountCode
  type: string
- container: ''
  name: transferCode
  type: string
- container: set
  name: invalidFields
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-funds-transfer-funds-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
