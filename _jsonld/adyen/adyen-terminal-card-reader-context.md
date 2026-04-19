---
class_count: 2
classes:
- CardReaderAPDURequest
- CardReaderAPDUResponse
context_file: json-ld/adyen-terminal-card-reader-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-card-reader-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Card Reader from Adyen.
layout: jsonld
name: Adyen Terminal Card Reader Context
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
  name: APDUClass
  type: string
- container: ''
  name: APDUInstruction
  type: string
- container: ''
  name: APDUPar1
  type: string
- container: ''
  name: APDUPar2
  type: string
- container: ''
  name: APDUData
  type: string
- container: ''
  name: APDUExpectedLength
  type: string
- container: ''
  name: Response
  type: string
- container: ''
  name: CardStatusWords
  type: string
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-card-reader-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
