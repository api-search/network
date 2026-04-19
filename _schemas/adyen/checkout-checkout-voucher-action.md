---
description: CheckoutVoucherAction schema from Adyen API
layout: schema
name: CheckoutVoucherAction
properties_list:
- description: The voucher alternative reference code.
  name: alternativeReference
  type: string
- description: A collection institution number (store number) for Econtext Pay-Easy ATM.
  name: collectionInstitutionNumber
  type: string
- description: The URL to download the voucher.
  name: downloadUrl
  type: string
- description: An entity number of Multibanco.
  name: entity
  type: string
- description: The date time of the voucher expiry.
  name: expiresAt
  type: string
- description: The initial amount.
  name: initialAmount
  type: object
- description: The URL to the detailed instructions to make payment using the voucher.
  name: instructionsUrl
  type: string
- description: The issuer of the voucher.
  name: issuer
  type: string
- description: The shopper telephone number (partially masked).
  name: maskedTelephoneNumber
  type: string
- description: The merchant name.
  name: merchantName
  type: string
- description: The merchant reference.
  name: merchantReference
  type: string
- description: A base64 encoded signature of all properties
  name: passCreationToken
  type: string
- description: Encoded payment data.
  name: paymentData
  type: string
- description: Specifies the payment method.
  name: paymentMethodType
  type: string
- description: The voucher reference code.
  name: reference
  type: string
- description: The shopper email.
  name: shopperEmail
  type: string
- description: The shopper name.
  name: shopperName
  type: string
- description: The surcharge amount.
  name: surcharge
  type: object
- description: The total amount (initial plus surcharge amount).
  name: totalAmount
  type: object
- description: '**voucher**'
  name: type
  type: string
- description: Specifies the URL to redirect to.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-voucher-action-schema.json
slug: checkout-checkout-voucher-action
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutVoucherAction
---
