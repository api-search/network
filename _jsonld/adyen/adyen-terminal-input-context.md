---
class_count: 1
classes:
- Input
context_file: json-ld/adyen-terminal-input-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-input-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Input from Adyen.
layout: jsonld
name: Adyen Terminal Input Context
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
  name: InputCommand
  type: string
- container: ''
  name: ConfirmedFlag
  type: boolean
- container: ''
  name: FunctionKey
  type: integer
- container: ''
  name: TextInput
  type: string
- container: ''
  name: DigitInput
  type: integer
- container: ''
  name: Password
  type: string
- container: set
  name: MenuEntryNumber
  type: integer
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-input-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
