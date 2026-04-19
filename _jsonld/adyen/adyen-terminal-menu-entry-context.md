---
class_count: 2
classes:
- MenuEntry
- MenuEntryTag
context_file: json-ld/adyen-terminal-menu-entry-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-menu-entry-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Menu Entry from Adyen.
layout: jsonld
name: Adyen Terminal Menu Entry Context
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
  name: DefaultSelectedFlag
  type: boolean
- container: ''
  name: OutputFormat
  type: string
- container: ''
  name: PredefinedContent
  type: string
- container: set
  name: OutputText
  type: string
- container: ''
  name: OutputXHTML
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-menu-entry-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
