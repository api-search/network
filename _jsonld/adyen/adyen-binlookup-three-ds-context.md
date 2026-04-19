---
class_count: 2
classes:
- ThreeDSAvailabilityRequest
- ThreeDSAvailabilityResponse
context_file: json-ld/adyen-binlookup-three-ds-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-binlookup-three-ds-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Binlookup Three Ds from Adyen.
layout: jsonld
name: Adyen Binlookup Three Ds Context
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
- container: set
  name: brands
  type: string
- container: ''
  name: cardNumber
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: recurringDetailReference
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: binDetails
  type: string
- container: set
  name: dsPublicKeys
  type: string
- container: ''
  name: threeDS1Supported
  type: boolean
- container: set
  name: threeDS2CardRangeDetails
  type: string
- container: ''
  name: threeDS2supported
  type: boolean
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-binlookup-three-ds-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
