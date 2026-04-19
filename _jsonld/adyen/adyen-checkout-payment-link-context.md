---
class_count: 4
classes:
- PaymentLinkRequest
- PaymentLinkResponse
- description
- url
context_file: json-ld/adyen-checkout-payment-link-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-payment-link-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Payment Link from Adyen.
layout: jsonld
name: Adyen Checkout Payment Link Context
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
  name: countryCode
  type: string
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: deliverAt
  type: dateTime
- container: ''
  name: deliveryAddress
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: installmentOptions
  type: reference
- container: set
  name: lineItems
  type: string
- container: ''
  name: manualCapture
  type: boolean
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
  name: recurringProcessingModel
  type: string
- container: ''
  name: reference
  type: string
- container: set
  name: requiredShopperFields
  type: string
- container: ''
  name: returnUrl
  type: string
- container: ''
  name: reusable
  type: boolean
- container: ''
  name: riskData
  type: string
- container: ''
  name: shopperEmail
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
  name: showRemovePaymentMethodButton
  type: boolean
- container: ''
  name: socialSecurityNumber
  type: string
- container: ''
  name: splitCardFundingSources
  type: boolean
- container: set
  name: splits
  type: string
- container: ''
  name: store
  type: string
- container: ''
  name: storePaymentMethodMode
  type: string
- container: ''
  name: telephoneNumber
  type: string
- container: ''
  name: themeId
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: updatedAt
  type: dateTime
property_count: 40
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-payment-link-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
