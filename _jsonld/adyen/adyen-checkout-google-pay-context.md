---
class_count: 2
classes:
- GooglePayDetails
- GooglePayDonations
context_file: json-ld/adyen-checkout-google-pay-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-google-pay-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Google Pay from Adyen.
layout: jsonld
name: Adyen Checkout Google Pay Context
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
  name: checkoutAttemptId
  type: string
- container: ''
  name: fundingSource
  type: string
- container: ''
  name: googlePayCardNetwork
  type: string
- container: ''
  name: googlePayToken
  type: string
- container: ''
  name: recurringDetailReference
  type: string
- container: ''
  name: storedPaymentMethodId
  type: string
- container: ''
  name: type
  type: string
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-google-pay-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
