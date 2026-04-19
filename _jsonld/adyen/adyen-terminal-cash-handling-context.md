---
class_count: 1
classes:
- CashHandlingDevice
context_file: json-ld/adyen-terminal-cash-handling-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-cash-handling-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Cash Handling from Adyen.
layout: jsonld
name: Adyen Terminal Cash Handling Context
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
  name: CashHandlingOKFlag
  type: boolean
- container: ''
  name: Currency
  type: string
- container: set
  name: CoinsOrBills
  type: string
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-cash-handling-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
