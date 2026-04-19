---
class_count: 4
classes:
- StoredPaymentMethodDetails
- StoredPaymentMethodResource
- StoredPaymentMethod
- name
context_file: json-ld/adyen-checkout-stored-payment-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-stored-payment-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Stored Payment from Adyen.
layout: jsonld
name: Adyen Checkout Stored Payment Context
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
  name: recurringDetailReference
  type: string
- container: ''
  name: storedPaymentMethodId
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: expiryMonth
  type: string
- container: ''
  name: expiryYear
  type: string
- container: ''
  name: externalResponseCode
  type: string
- container: ''
  name: externalTokenReference
  type: string
- container: ''
  name: holderName
  type: string
- container: ''
  name: iban
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: issuerName
  type: string
- container: ''
  name: lastFour
  type: string
- container: ''
  name: networkTxReference
  type: string
- container: ''
  name: ownerName
  type: string
- container: ''
  name: shopperEmail
  type: string
- container: ''
  name: shopperReference
  type: string
- container: set
  name: supportedRecurringProcessingModels
  type: string
- container: ''
  name: bankAccountNumber
  type: string
- container: ''
  name: bankLocationId
  type: string
- container: ''
  name: label
  type: string
- container: set
  name: supportedShopperInteractions
  type: string
property_count: 23
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-stored-payment-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
