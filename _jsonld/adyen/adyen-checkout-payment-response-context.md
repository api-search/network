---
class_count: 1
classes:
- PaymentResponse
context_file: json-ld/adyen-checkout-payment-response-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-payment-response-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Payment Response from Adyen.
layout: jsonld
name: Adyen Checkout Payment Response Context
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
  name: action
  type: string
- container: ''
  name: additionalData
  type: reference
- container: ''
  name: amount
  type: string
- container: ''
  name: donationToken
  type: string
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
  name: paymentMethod
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
  name: threeDS2ResponseData
  type: string
- container: ''
  name: threeDS2Result
  type: string
- container: ''
  name: threeDSPaymentData
  type: string
property_count: 15
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-payment-response-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
