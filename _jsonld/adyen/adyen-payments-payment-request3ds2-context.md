---
class_count: 1
classes:
- PaymentRequest3ds2
context_file: json-ld/adyen-payments-payment-request3ds2-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payments-payment-request3ds2-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payments Payment Request3Ds2 from Adyen.
layout: jsonld
name: Adyen Payments Payment Request3Ds2 Context
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
  name: accountInfo
  type: string
- container: ''
  name: additionalAmount
  type: string
- container: ''
  name: additionalData
  type: reference
- container: ''
  name: amount
  type: string
- container: ''
  name: applicationInfo
  type: string
- container: ''
  name: billingAddress
  type: string
- container: ''
  name: browserInfo
  type: string
- container: ''
  name: captureDelayHours
  type: integer
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: dccQuote
  type: string
- container: ''
  name: deliveryAddress
  type: string
- container: ''
  name: deliveryDate
  type: dateTime
- container: ''
  name: deviceFingerprint
  type: string
- container: ''
  name: fraudOffset
  type: integer
- container: ''
  name: installments
  type: string
- container: ''
  name: localizedShopperStatement
  type: reference
- container: ''
  name: mcc
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: merchantOrderReference
  type: string
- container: ''
  name: merchantRiskIndicator
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: orderReference
  type: string
- container: ''
  name: recurring
  type: string
- container: ''
  name: recurringProcessingModel
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: selectedBrand
  type: string
- container: ''
  name: selectedRecurringDetailReference
  type: string
- container: ''
  name: sessionId
  type: string
- container: ''
  name: shopperEmail
  type: string
- container: ''
  name: shopperIP
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: shopperLocale
  type: string
- container: ''
  name: shopperName
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: shopperStatement
  type: string
- container: ''
  name: socialSecurityNumber
  type: string
- container: set
  name: splits
  type: string
- container: ''
  name: store
  type: string
- container: ''
  name: telephoneNumber
  type: string
- container: ''
  name: threeDS2RequestData
  type: string
- container: ''
  name: threeDS2Result
  type: string
- container: ''
  name: threeDS2Token
  type: string
- container: ''
  name: threeDSAuthenticationOnly
  type: boolean
- container: ''
  name: totalsGroup
  type: string
- container: ''
  name: trustedShopper
  type: boolean
property_count: 45
provider_name: Adyen
provider_slug: adyen
slug: adyen-payments-payment-request3ds2-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
