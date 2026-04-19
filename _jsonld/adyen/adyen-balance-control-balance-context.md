---
class_count: 3
classes:
- BalanceTransferRequest
- BalanceTransferResponse
- description
context_file: json-ld/adyen-balance-control-balance-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-balance-control-balance-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Balance Control Balance from Adyen.
layout: jsonld
name: Adyen Balance Control Balance Context
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
  name: fromMerchant
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: toMerchant
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: pspReference
  type: string
- container: ''
  name: status
  type: string
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-balance-control-balance-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
