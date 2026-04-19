---
class_count: 2
classes:
- CancelOrderRequest
- CancelOrderResponse
context_file: json-ld/adyen-checkout-cancel-order-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-cancel-order-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Cancel Order from Adyen.
layout: jsonld
name: Adyen Checkout Cancel Order Context
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
  name: merchantAccount
  type: string
- container: ''
  name: order
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-cancel-order-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
