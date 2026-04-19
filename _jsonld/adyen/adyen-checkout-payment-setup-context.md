---
class_count: 2
classes:
- PaymentSetupRequest
- PaymentSetupResponse
context_file: json-ld/adyen-checkout-payment-setup-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-payment-setup-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Payment Setup from Adyen.
layout: jsonld
name: Adyen Checkout Payment Setup Context
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
  name: additionalAmount
  type: string
- container: ''
  name: additionalData
  type: reference
- container: set
  name: allowedPaymentMethods
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: applicationInfo
  type: string
- container: ''
  name: billingAddress
  type: string
- container: set
  name: blockedPaymentMethods
  type: string
- container: ''
  name: captureDelayHours
  type: integer
- container: ''
  name: channel
  type: string
- container: ''
  name: checkoutAttemptId
  type: string
- container: ''
  name: company
  type: string
- container: ''
  name: configuration
  type: string
- container: ''
  name: conversionId
  type: string
- container: ''
  name: countryCode
  type: string
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
  name: enableOneClick
  type: boolean
- container: ''
  name: enablePayOut
  type: boolean
- container: ''
  name: enableRecurring
  type: boolean
- container: ''
  name: entityType
  type: string
- container: ''
  name: fraudOffset
  type: integer
- container: ''
  name: installments
  type: string
- container: set
  name: lineItems
  type: string
- container: ''
  name: localizedShopperStatement
  type: reference
- container: ''
  name: mandate
  type: string
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
  name: metadata
  type: reference
- container: ''
  name: orderReference
  type: string
- container: ''
  name: origin
  type: string
- container: ''
  name: platformChargebackLogic
  type: string
- container: ''
  name: recurringExpiry
  type: string
- container: ''
  name: recurringFrequency
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: returnUrl
  type: string
- container: ''
  name: riskData
  type: string
- container: ''
  name: sdkVersion
  type: string
- container: ''
  name: sessionValidity
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
  name: storePaymentMethod
  type: boolean
- container: ''
  name: telephoneNumber
  type: string
- container: ''
  name: threeDSAuthenticationOnly
  type: boolean
- container: ''
  name: token
  type: string
- container: ''
  name: trustedShopper
  type: boolean
- container: ''
  name: paymentSession
  type: string
- container: set
  name: recurringDetails
  type: string
property_count: 58
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-payment-setup-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
