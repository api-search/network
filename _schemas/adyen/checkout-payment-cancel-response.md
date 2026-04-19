---
description: PaymentCancelResponse schema from Adyen API
layout: schema
name: PaymentCancelResponse
properties_list:
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: The [`pspReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to cancel.
  name: paymentPspReference
  type: string
- description: Adyen's 16-character reference associated with the cancel request.
  name: pspReference
  type: string
- description: Your reference for the cancel request.
  name: reference
  type: string
- description: The status of your request. This will always have the value **received**.
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-cancel-response-schema.json
slug: checkout-payment-cancel-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentCancelResponse
---
