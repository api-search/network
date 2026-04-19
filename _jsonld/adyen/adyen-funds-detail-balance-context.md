---
class_count: 1
classes:
- DetailBalance
context_file: json-ld/adyen-funds-detail-balance-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-funds-detail-balance-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Funds Detail Balance from Adyen.
layout: jsonld
name: Adyen Funds Detail Balance Context
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
- container: set
  name: balance
  type: string
- container: set
  name: onHoldBalance
  type: string
- container: set
  name: pendingBalance
  type: string
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-funds-detail-balance-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
