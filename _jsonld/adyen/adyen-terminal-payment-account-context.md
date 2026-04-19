---
class_count: 2
classes:
- PaymentAccountReq
- PaymentAccountStatus
context_file: json-ld/adyen-terminal-payment-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-payment-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Payment Account from Adyen.
layout: jsonld
name: Adyen Terminal Payment Account Context
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
  name: AccountType
  type: string
- container: ''
  name: CardAcquisitionReference
  type: string
- container: ''
  name: PaymentInstrumentData
  type: string
- container: ''
  name: CurrentBalance
  type: decimal
- container: ''
  name: Currency
  type: string
- container: ''
  name: PaymentAcquirerData
  type: string
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-payment-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
