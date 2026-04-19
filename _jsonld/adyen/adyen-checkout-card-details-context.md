---
class_count: 3
classes:
- CardDetailsRequest
- CardDetailsResponse
- CardDetails
context_file: json-ld/adyen-checkout-card-details-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-card-details-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Card Details from Adyen.
layout: jsonld
name: Adyen Checkout Card Details Context
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
  name: cardNumber
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: encryptedCardNumber
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: set
  name: supportedBrands
  type: string
- container: set
  name: brands
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: checkoutAttemptId
  type: string
- container: ''
  name: cupsecureplus.smscode
  type: string
- container: ''
  name: cvc
  type: string
- container: ''
  name: encryptedExpiryMonth
  type: string
- container: ''
  name: encryptedExpiryYear
  type: string
- container: ''
  name: encryptedSecurityCode
  type: string
- container: ''
  name: expiryMonth
  type: string
- container: ''
  name: expiryYear
  type: string
- container: ''
  name: fundingSource
  type: string
- container: ''
  name: holderName
  type: string
- container: ''
  name: networkPaymentReference
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: recurringDetailReference
  type: string
- container: ''
  name: shopperNotificationReference
  type: string
- container: ''
  name: storedPaymentMethodId
  type: string
- container: ''
  name: threeDS2SdkVersion
  type: string
- container: ''
  name: type
  type: string
property_count: 24
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-card-details-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
