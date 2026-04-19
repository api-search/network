---
description: CardDetailsRequest schema from Adyen API
layout: schema
name: CardDetailsRequest
properties_list:
- description: A minimum of the first 8 digits of the card number and a maximum of the full card number. 11 digits gives the best result. You must be [fully PCI compliant](https://docs.adyen.com/development-resource
  name: cardNumber
  type: string
- description: 'The shopper country. Format: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) Example: NL or DE'
  name: countryCode
  type: string
- description: The encrypted card number.
  name: encryptedCardNumber
  type: string
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The card brands you support. This is the [`brands`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/paymentMethods__resParam_paymentMethods-brands) array from your [`/paymentMethods`
  name: supportedBrands
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-card-details-request-schema.json
slug: checkout-card-details-request
tags:
- Payments
- Financial Services
- Fintech
title: CardDetailsRequest
---
