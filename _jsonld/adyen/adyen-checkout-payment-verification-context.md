---
class_count: 2
classes:
- PaymentVerificationRequest
- PaymentVerificationResponse
context_file: json-ld/adyen-checkout-payment-verification-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-payment-verification-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Payment Verification from Adyen.
layout: jsonld
name: Adyen Checkout Payment Verification Context
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
  name: payload
  type: string
- container: ''
  name: additionalData
  type: reference
- container: ''
  name: fraudResult
  type: string
- container: ''
  name: merchantReference
  type: string
- container: ''
  name: order
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: refusalReason
  type: string
- container: ''
  name: refusalReasonCode
  type: string
- container: ''
  name: resultCode
  type: string
- container: ''
  name: serviceError
  type: string
- container: ''
  name: shopperLocale
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-payment-verification-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
