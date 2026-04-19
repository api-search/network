---
description: PaymentMethodsRequest schema from Adyen API
layout: schema
name: PaymentMethodsRequest
properties_list:
- description: This field contains additional data, which may be required for a particular payment request. The `additionalData` object consists of entries, each of which includes the key and value.
  name: additionalData
  type: object
- description: 'List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types). Example: `"allowedPay'
  name: allowedPaymentMethods
  type: array
- description: The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/
  name: amount
  type: object
- description: 'List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types). Example: `"blockedPaym'
  name: blockedPaymentMethods
  type: array
- description: 'The platform where a payment transaction takes place. This field can be used for filtering out payment methods that are only available on specific platforms. Possible values: * iOS * Android * Web'
  name: channel
  type: string
- description: The shopper's country code.
  name: countryCode
  type: string
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The order information required for partial payments.
  name: order
  type: object
- description: The combination of a language code and a country code to specify the language to be used in the payment.
  name: shopperLocale
  type: string
- description: 'Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identif'
  name: shopperReference
  type: string
- description: Boolean value indicating whether the card payment method should be split into separate debit and credit options.
  name: splitCardFundingSources
  type: boolean
- description: Required for Adyen for Platforms integrations if you have a platform setup. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-referen
  name: store
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-methods-request-schema.json
slug: checkout-payment-methods-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentMethodsRequest
---
