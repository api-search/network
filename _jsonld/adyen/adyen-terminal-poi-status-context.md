---
class_count: 1
classes:
- POIStatus
context_file: json-ld/adyen-terminal-poi-status-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-poi-status-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Poi Status from Adyen.
layout: jsonld
name: Adyen Terminal Poi Status Context
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
  name: GlobalStatus
  type: string
- container: ''
  name: SecurityOKFlag
  type: boolean
- container: ''
  name: PEDOKFlag
  type: boolean
- container: ''
  name: CardReaderOKFlag
  type: boolean
- container: ''
  name: PrinterStatus
  type: string
- container: ''
  name: CommunicationOKFlag
  type: boolean
- container: set
  name: CashHandlingDevice
  type: string
- container: ''
  name: FraudPreventionFlag
  type: boolean
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-poi-status-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
