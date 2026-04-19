---
description: PaymentAmountUpdateResponse schema from Adyen API
layout: schema
name: PaymentAmountUpdateResponse
properties_list:
- description: The updated amount.
  name: amount
  type: object
- description: 'The reason for the amount update. Possible values: * **delayedCharge** * **noShow** * **installment**'
  name: industryUsage
  type: string
- description: Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). > This field is required for partial refunds with 3
  name: lineItems
  type: array
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to update.
  name: paymentPspReference
  type: string
- description: Adyen's 16-character reference associated with the amount update request.
  name: pspReference
  type: string
- description: 'Your reference for the amount update request. Maximum length: 80 characters.'
  name: reference
  type: string
- description: An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-a
  name: splits
  type: array
- description: The status of your request. This will always have the value **received**.
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-amount-update-response-schema.json
slug: checkout-payment-amount-update-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentAmountUpdateResponse
---
