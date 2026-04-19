---
description: PaymentRefundResponse schema from Adyen API
layout: schema
name: PaymentRefundResponse
properties_list:
- description: The refund amount.
  name: amount
  type: object
- description: Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). > This field is required for partial refunds with 3
  name: lineItems
  type: array
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: Your reason for the refund request.
  name: merchantRefundReason
  type: string
- description: The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to refund.
  name: paymentPspReference
  type: string
- description: Adyen's 16-character reference associated with the refund request.
  name: pspReference
  type: string
- description: Your reference for the refund request.
  name: reference
  type: string
- description: An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-a
  name: splits
  type: array
- description: The status of your request. This will always have the value **received**.
  name: status
  type: string
- description: The online store or [physical store](https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/#create-stores) that is processing the refund. This must be the same as th
  name: store
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-refund-response-schema.json
slug: checkout-payment-refund-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentRefundResponse
---
