---
class_count: 1
classes:
- SensitiveCardData
context_file: json-ld/adyen-terminal-sensitive-card-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-sensitive-card-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Sensitive Card from Adyen.
layout: jsonld
name: Adyen Terminal Sensitive Card Context
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
  name: PAN
  type: integer
- container: ''
  name: CardSeqNumb
  type: integer
- container: ''
  name: ExpiryDate
  type: integer
- container: set
  name: TrackData
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-sensitive-card-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
