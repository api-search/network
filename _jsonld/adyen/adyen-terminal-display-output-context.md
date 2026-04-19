---
class_count: 1
classes:
- DisplayOutput
context_file: json-ld/adyen-terminal-display-output-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-display-output-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Display Output from Adyen.
layout: jsonld
name: Adyen Terminal Display Output Context
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
  name: ResponseRequiredFlag
  type: boolean
- container: ''
  name: MinimumDisplayTime
  type: integer
- container: ''
  name: Device
  type: string
- container: ''
  name: InfoQualify
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
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-display-output-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
