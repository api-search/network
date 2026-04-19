---
class_count: 1
classes:
- MerchantAccount
context_file: json-ld/adyen-pos-terminal-merchant-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-pos-terminal-merchant-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Pos Terminal Merchant from Adyen.
layout: jsonld
name: Adyen Pos Terminal Merchant Context
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
- container: set
  name: inStoreTerminals
  type: string
- container: set
  name: inventoryTerminals
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: set
  name: stores
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-pos-terminal-merchant-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
