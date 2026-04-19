---
class_count: 1
classes:
- AchDetails
context_file: json-ld/adyen-checkout-ach-details-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-ach-details-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Ach Details from Adyen.
layout: jsonld
name: Adyen Checkout Ach Details Context
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
  name: bankAccountNumber
  type: string
- container: ''
  name: bankAccountType
  type: string
- container: ''
  name: bankLocationId
  type: string
- container: ''
  name: checkoutAttemptId
  type: string
- container: ''
  name: encryptedBankAccountNumber
  type: string
- container: ''
  name: encryptedBankLocationId
  type: string
- container: ''
  name: ownerName
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
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-ach-details-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
