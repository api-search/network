---
class_count: 1
classes:
- AdjustAuthorisationRequest
context_file: json-ld/adyen-payments-adjust-authorisation-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payments-adjust-authorisation-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payments Adjust Authorisation from Adyen.
layout: jsonld
name: Adyen Payments Adjust Authorisation Context
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
  name: merchantAccount
  type: string
- container: ''
  name: modificationAmount
  type: string
- container: ''
  name: mpiData
  type: string
- container: ''
  name: originalMerchantReference
  type: string
- container: ''
  name: originalReference
  type: string
- container: ''
  name: platformChargebackLogic
  type: string
- container: ''
  name: reference
  type: string
- container: set
  name: splits
  type: string
- container: ''
  name: tenderReference
  type: string
- container: ''
  name: uniqueTerminalId
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-payments-adjust-authorisation-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
