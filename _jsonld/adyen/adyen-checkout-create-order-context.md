---
class_count: 2
classes:
- CreateOrderRequest
- CreateOrderResponse
context_file: json-ld/adyen-checkout-create-order-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-create-order-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Create Order from Adyen.
layout: jsonld
name: Adyen Checkout Create Order Context
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
  name: expiresAt
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: additionalData
  type: reference
- container: ''
  name: fraudResult
  type: string
- container: ''
  name: orderData
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: refusalReason
  type: string
- container: ''
  name: remainingAmount
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-create-order-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
