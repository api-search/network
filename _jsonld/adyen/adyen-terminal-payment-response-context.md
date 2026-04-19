---
class_count: 1
classes:
- PaymentResponse
context_file: json-ld/adyen-terminal-payment-response-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-payment-response-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Payment Response from Adyen.
layout: jsonld
name: Adyen Terminal Payment Response Context
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
  name: Response
  type: string
- container: ''
  name: SaleData
  type: string
- container: ''
  name: POIData
  type: string
- container: ''
  name: PaymentResult
  type: string
- container: set
  name: LoyaltyResult
  type: string
- container: set
  name: PaymentReceipt
  type: string
- container: set
  name: CustomerOrder
  type: string
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-payment-response-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
