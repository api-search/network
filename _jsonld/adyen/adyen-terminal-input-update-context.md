---
class_count: 1
classes:
- InputUpdate
context_file: json-ld/adyen-terminal-input-update-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-input-update-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Input Update from Adyen.
layout: jsonld
name: Adyen Terminal Input Update Context
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
  name: MessageReference
  type: string
- container: ''
  name: OutputContent
  type: string
- container: set
  name: MenuEntry
  type: string
- container: ''
  name: OutputSignature
  type: string
- container: ''
  name: MinLength
  type: integer
- container: ''
  name: MaxLength
  type: integer
- container: ''
  name: MaxDecimalLength
  type: integer
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-input-update-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
