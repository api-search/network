---
class_count: 8
classes:
- PaymentInstrumentGroupInfo
- PaymentInstrumentGroup
- PaymentInstrumentInfo
- PaymentInstrumentRequirement
- PaymentInstrumentRevealInfo
- PaymentInstrument
- PaymentInstrumentUpdateRequest
- description
context_file: json-ld/adyen-configuration-payment-instrument-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-payment-instrument-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Payment Instrument from Adyen.
layout: jsonld
name: Adyen Configuration Payment Instrument Context
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
  name: balancePlatform
  type: string
- container: ''
  name: properties
  type: reference
- container: ''
  name: reference
  type: string
- container: ''
  name: txVariant
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: balanceAccountId
  type: string
- container: ''
  name: bankAccount
  type: string
- container: ''
  name: card
  type: string
- container: ''
  name: issuingCountryCode
  type: string
- container: ''
  name: paymentInstrumentGroupId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: onlyForCrossBalancePlatform
  type: boolean
- container: ''
  name: paymentInstrumentType
  type: string
- container: ''
  name: cvc
  type: string
- container: ''
  name: expiration
  type: string
- container: ''
  name: pan
  type: string
- container: ''
  name: statusComment
  type: string
property_count: 19
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-payment-instrument-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
