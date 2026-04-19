---
class_count: 1
classes:
- SubInputDetail
context_file: json-ld/adyen-checkout-sub-input-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-sub-input-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Sub Input from Adyen.
layout: jsonld
name: Adyen Checkout Sub Input Context
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
  name: configuration
  type: reference
- container: set
  name: items
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: optional
  type: boolean
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: string
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-sub-input-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
