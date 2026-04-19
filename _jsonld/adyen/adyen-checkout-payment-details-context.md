---
class_count: 3
classes:
- PaymentDetailsRequest
- PaymentDetailsResponse
- PaymentDetails
context_file: json-ld/adyen-checkout-payment-details-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-payment-details-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Payment Details from Adyen.
layout: jsonld
name: Adyen Checkout Payment Details Context
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
  name: authenticationData
  type: string
- container: ''
  name: details
  type: string
- container: ''
  name: paymentData
  type: string
- container: ''
  name: threeDSAuthenticationOnly
  type: boolean
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
  name: shopperLocale
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
- container: ''
  name: checkoutAttemptId
  type: string
- container: ''
  name: type
  type: string
property_count: 21
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-payment-details-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
