---
class_count: 2
classes:
- FindTerminalRequest
- FindTerminalResponse
context_file: json-ld/adyen-pos-terminal-find-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-pos-terminal-find-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Pos Terminal Find from Adyen.
layout: jsonld
name: Adyen Pos Terminal Find Context
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
  name: terminal
  type: string
- container: ''
  name: companyAccount
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: merchantInventory
  type: boolean
- container: ''
  name: store
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-pos-terminal-find-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
