---
class_count: 1
classes:
- Rebates
context_file: json-ld/adyen-terminal-rebates-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-rebates-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Rebates from Adyen.
layout: jsonld
name: Adyen Terminal Rebates Context
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
  name: TotalRebate
  type: decimal
- container: ''
  name: RebateLabel
  type: string
- container: set
  name: SaleItemRebate
  type: string
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-rebates-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
