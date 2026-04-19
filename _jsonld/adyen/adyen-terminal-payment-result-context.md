---
class_count: 1
classes:
- PaymentResult
context_file: json-ld/adyen-terminal-payment-result-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-payment-result-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Payment Result from Adyen.
layout: jsonld
name: Adyen Terminal Payment Result Context
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
  name: PaymentInstrumentData
  type: string
- container: ''
  name: AmountsResp
  type: string
- container: ''
  name: Instalment
  type: string
- container: set
  name: CurrencyConversion
  type: string
- container: ''
  name: MerchantOverrideFlag
  type: boolean
- container: ''
  name: CapturedSignature
  type: string
- container: ''
  name: ProtectedSignature
  type: string
- container: ''
  name: CustomerLanguage
  type: string
- container: ''
  name: OnlineFlag
  type: boolean
- container: ''
  name: AuthenticationMethod
  type: string
- container: ''
  name: ValidityDate
  type: date
- container: ''
  name: PaymentAcquirerData
  type: string
property_count: 13
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-payment-result-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
