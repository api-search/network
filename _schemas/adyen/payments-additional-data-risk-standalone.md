---
description: AdditionalDataRiskStandalone schema from Adyen API
layout: schema
name: AdditionalDataRiskStandalone
properties_list:
- description: Shopper's country of residence in the form of ISO standard 3166 2-character country codes.
  name: PayPal.CountryCode
  type: string
- description: Shopper's email.
  name: PayPal.EmailId
  type: string
- description: Shopper's first name.
  name: PayPal.FirstName
  type: string
- description: Shopper's last name.
  name: PayPal.LastName
  type: string
- description: 'Unique PayPal Customer Account identification number. Character length and limitations: 13 single-byte alphanumeric characters.'
  name: PayPal.PayerId
  type: string
- description: Shopper's phone number.
  name: PayPal.Phone
  type: string
- description: 'Allowed values: * **Eligible** — Merchant is protected by PayPal''s Seller Protection Policy for Unauthorized Payments and Item Not Received. * **PartiallyEligible** — Merchant is protected by PayPal''s'
  name: PayPal.ProtectionEligibility
  type: string
- description: Unique transaction ID of the payment.
  name: PayPal.TransactionId
  type: string
- description: 'Raw AVS result received from the acquirer, where available. Example: D'
  name: avsResultRaw
  type: string
- description: The Bank Identification Number of a credit card, which is the first six digits of a card number. Required for [tokenized card request](https://docs.adyen.com/risk-management/standalone-risk#tokenised-
  name: bin
  type: string
- description: 'Raw CVC result received from the acquirer, where available. Example: 1'
  name: cvcResultRaw
  type: string
- description: Unique identifier or token for the shopper's card details.
  name: riskToken
  type: string
- description: 'A Boolean value indicating whether 3DS authentication was completed on this payment. Example: true'
  name: threeDAuthenticated
  type: string
- description: 'A Boolean value indicating whether 3DS was offered for this payment. Example: true'
  name: threeDOffered
  type: string
- description: 'Required for PayPal payments only. The only supported value is: **paypal**.'
  name: tokenDataType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-additional-data-risk-standalone-schema.json
slug: payments-additional-data-risk-standalone
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataRiskStandalone
---
