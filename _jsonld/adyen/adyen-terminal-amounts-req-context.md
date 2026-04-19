---
class_count: 1
classes:
- AmountsReq
context_file: json-ld/adyen-terminal-amounts-req-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-amounts-req-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Amounts Req from Adyen.
layout: jsonld
name: Adyen Terminal Amounts Req Context
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
  name: RequestedAmount
  type: decimal
- container: ''
  name: CashBackAmount
  type: decimal
- container: ''
  name: TipAmount
  type: decimal
- container: ''
  name: PaidAmount
  type: decimal
- container: ''
  name: MinimumAmountToDeliver
  type: decimal
- container: ''
  name: MaximumCashBackAmount
  type: decimal
- container: ''
  name: MinimumSplitAmount
  type: decimal
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-amounts-req-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
