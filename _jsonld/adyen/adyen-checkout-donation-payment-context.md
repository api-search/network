---
class_count: 2
classes:
- DonationPaymentRequest
- DonationPaymentResponse
context_file: json-ld/adyen-checkout-donation-payment-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-donation-payment-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Donation Payment from Adyen.
layout: jsonld
name: Adyen Checkout Donation Payment Context
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
  name: additionalData
  type: reference
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
- container: ''
  name: browserInfo
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: checkoutAttemptId
  type: string
- container: ''
  name: conversionId
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: dateOfBirth
  type: dateTime
- container: ''
  name: deliverAt
  type: dateTime
- container: ''
  name: deliveryAddress
  type: string
- container: ''
  name: deviceFingerprint
  type: string
- container: ''
  name: donationAccount
  type: string
- container: ''
  name: donationOriginalPspReference
  type: string
- container: ''
  name: donationToken
  type: string
- container: set
  name: lineItems
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: merchantRiskIndicator
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: mpiData
  type: string
- container: ''
  name: origin
  type: string
- container: ''
  name: paymentMethod
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
  name: socialSecurityNumber
  type: string
- container: ''
  name: telephoneNumber
  type: string
- container: ''
  name: threeDS2RequestData
  type: string
- container: ''
  name: threeDSAuthenticationOnly
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: payment
  type: string
- container: ''
  name: status
  type: string
property_count: 44
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-donation-payment-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
