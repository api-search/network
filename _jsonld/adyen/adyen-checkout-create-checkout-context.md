---
class_count: 3
classes:
- CreateCheckoutSessionRequest
- CreateCheckoutSessionResponse
- url
context_file: json-ld/adyen-checkout-create-checkout-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-create-checkout-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Create Checkout from Adyen.
layout: jsonld
name: Adyen Checkout Create Checkout Context
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
  name: authenticationData
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
  name: company
  type: string
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
  name: enableOneClick
  type: boolean
- container: ''
  name: enablePayOut
  type: boolean
- container: ''
  name: enableRecurring
  type: boolean
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: fundOrigin
  type: string
- container: ''
  name: fundRecipient
  type: string
- container: ''
  name: installmentOptions
  type: reference
- container: set
  name: lineItems
  type: string
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
  name: mode
  type: string
- container: ''
  name: mpiData
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
  name: recurringProcessingModel
  type: string
- container: ''
  name: redirectFromIssuerMethod
  type: string
- container: ''
  name: redirectToIssuerMethod
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
  name: showInstallmentAmount
  type: boolean
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
  name: storePaymentMethod
  type: boolean
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
  name: threeDSAuthenticationOnly
  type: boolean
- container: ''
  name: trustedShopper
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: sessionData
  type: string
property_count: 61
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-create-checkout-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
