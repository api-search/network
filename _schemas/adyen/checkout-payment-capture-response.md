---
description: PaymentCaptureResponse schema from Adyen API
layout: schema
name: PaymentCaptureResponse
properties_list:
- description: The captured amount.
  name: amount
  type: object
- description: Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). > This field is required for partial refunds with 3
  name: lineItems
  type: array
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to capture.
  name: paymentPspReference
  type: string
- description: Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#chargebacks-and-disputes).
  name: platformChargebackLogic
  type: object
- description: Adyen's 16-character reference associated with the capture request.
  name: pspReference
  type: string
- description: Your reference for the capture request.
  name: reference
  type: string
- description: An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-a
  name: splits
  type: array
- description: The status of your request. This will always have the value **received**.
  name: status
  type: string
- description: List of sub-merchants.
  name: subMerchants
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-capture-response-schema.json
slug: checkout-payment-capture-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentCaptureResponse
---
