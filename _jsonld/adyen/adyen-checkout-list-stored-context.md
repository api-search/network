---
class_count: 1
classes:
- ListStoredPaymentMethodsResponse
context_file: json-ld/adyen-checkout-list-stored-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-list-stored-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout List Stored from Adyen.
layout: jsonld
name: Adyen Checkout List Stored Context
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
  name: shopperReference
  type: string
- container: set
  name: storedPaymentMethods
  type: string
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-list-stored-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
