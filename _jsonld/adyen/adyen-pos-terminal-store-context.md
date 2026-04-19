---
class_count: 2
classes:
- Store
- description
context_file: json-ld/adyen-pos-terminal-store-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-pos-terminal-store-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Pos Terminal Store from Adyen.
layout: jsonld
name: Adyen Pos Terminal Store Context
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
  name: address
  type: string
- container: set
  name: inStoreTerminals
  type: string
- container: ''
  name: merchantAccountCode
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: store
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-pos-terminal-store-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
