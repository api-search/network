---
class_count: 2
classes:
- PaymentRefundRequest
- PaymentRefundResponse
context_file: json-ld/adyen-checkout-payment-refund-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-payment-refund-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Payment Refund from Adyen.
layout: jsonld
name: Adyen Checkout Payment Refund Context
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
  name: amount
  type: string
- container: ''
  name: applicationInfo
  type: string
- container: set
  name: lineItems
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: merchantRefundReason
  type: string
- container: ''
  name: reference
  type: string
- container: set
  name: splits
  type: string
- container: ''
  name: store
  type: string
- container: ''
  name: paymentPspReference
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: status
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-payment-refund-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
