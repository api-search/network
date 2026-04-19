---
class_count: 1
classes:
- PaymentData
context_file: json-ld/adyen-terminal-payment-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-payment-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Payment Data from Adyen.
layout: jsonld
name: Adyen Terminal Payment Data Context
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
  name: PaymentType
  type: string
- container: ''
  name: SplitPaymentFlag
  type: boolean
- container: ''
  name: RequestedValidityDate
  type: date
- container: ''
  name: CardAcquisitionReference
  type: string
- container: ''
  name: Instalment
  type: string
- container: ''
  name: CustomerOrder
  type: string
- container: ''
  name: PaymentInstrumentData
  type: string
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-payment-data-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
