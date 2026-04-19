---
class_count: 1
classes:
- PaymentRequest
context_file: json-ld/adyen-terminal-payment-request-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-payment-request-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Payment Request from Adyen.
layout: jsonld
name: Adyen Terminal Payment Request Context
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
  name: SaleData
  type: string
- container: ''
  name: PaymentTransaction
  type: string
- container: ''
  name: PaymentData
  type: string
- container: set
  name: LoyaltyData
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-payment-request-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
