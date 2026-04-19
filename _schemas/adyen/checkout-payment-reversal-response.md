---
description: PaymentReversalResponse schema from Adyen API
layout: schema
name: PaymentReversalResponse
properties_list:
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to reverse.
  name: paymentPspReference
  type: string
- description: Adyen's 16-character reference associated with the reversal request.
  name: pspReference
  type: string
- description: Your reference for the reversal request.
  name: reference
  type: string
- description: The status of your request. This will always have the value **received**.
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-reversal-response-schema.json
slug: checkout-payment-reversal-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentReversalResponse
---
