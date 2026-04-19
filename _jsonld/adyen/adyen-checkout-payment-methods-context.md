---
class_count: 2
classes:
- PaymentMethodsRequest
- PaymentMethodsResponse
context_file: json-ld/adyen-checkout-payment-methods-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-payment-methods-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Payment Methods from Adyen.
layout: jsonld
name: Adyen Checkout Payment Methods Context
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
  name: additionalData
  type: reference
- container: set
  name: allowedPaymentMethods
  type: string
- container: ''
  name: amount
  type: string
- container: set
  name: blockedPaymentMethods
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: order
  type: string
- container: ''
  name: shopperLocale
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: splitCardFundingSources
  type: boolean
- container: ''
  name: store
  type: string
- container: set
  name: paymentMethods
  type: string
- container: set
  name: storedPaymentMethods
  type: string
property_count: 14
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-payment-methods-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
