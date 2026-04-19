---
class_count: 2
classes:
- BalanceInquiryRequest
- BalanceInquiryResponse
context_file: json-ld/adyen-terminal-balance-inquiry-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-balance-inquiry-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Balance Inquiry from Adyen.
layout: jsonld
name: Adyen Terminal Balance Inquiry Context
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
  name: PaymentAccountReq
  type: string
- container: ''
  name: LoyaltyAccountReq
  type: string
- container: ''
  name: Response
  type: string
- container: ''
  name: PaymentAccountStatus
  type: string
- container: ''
  name: LoyaltyAccountStatus
  type: string
- container: set
  name: PaymentReceipt
  type: string
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-balance-inquiry-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
