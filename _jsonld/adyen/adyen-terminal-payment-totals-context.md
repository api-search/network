---
class_count: 1
classes:
- PaymentTotals
context_file: json-ld/adyen-terminal-payment-totals-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-payment-totals-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Payment Totals from Adyen.
layout: jsonld
name: Adyen Terminal Payment Totals Context
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
  name: TransactionType
  type: string
- container: ''
  name: TransactionCount
  type: integer
- container: ''
  name: TransactionAmount
  type: decimal
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-payment-totals-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
