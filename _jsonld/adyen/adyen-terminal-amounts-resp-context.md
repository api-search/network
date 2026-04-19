---
class_count: 1
classes:
- AmountsResp
context_file: json-ld/adyen-terminal-amounts-resp-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-amounts-resp-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Amounts Resp from Adyen.
layout: jsonld
name: Adyen Terminal Amounts Resp Context
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
  name: Currency
  type: string
- container: ''
  name: AuthorizedAmount
  type: decimal
- container: ''
  name: TotalRebatesAmount
  type: decimal
- container: ''
  name: TotalFeesAmount
  type: decimal
- container: ''
  name: CashBackAmount
  type: decimal
- container: ''
  name: TipAmount
  type: decimal
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-amounts-resp-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
