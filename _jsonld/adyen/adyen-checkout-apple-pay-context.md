---
class_count: 4
classes:
- ApplePayDetails
- ApplePayDonations
- ApplePaySessionRequest
- ApplePaySessionResponse
context_file: json-ld/adyen-checkout-apple-pay-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-apple-pay-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Apple Pay from Adyen.
layout: jsonld
name: Adyen Checkout Apple Pay Context
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
  name: applePayToken
  type: string
- container: ''
  name: checkoutAttemptId
  type: string
- container: ''
  name: fundingSource
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
- container: ''
  name: displayName
  type: string
- container: ''
  name: domainName
  type: string
- container: ''
  name: merchantIdentifier
  type: string
- container: ''
  name: data
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-apple-pay-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
