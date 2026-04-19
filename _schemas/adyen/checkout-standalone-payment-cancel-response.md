---
description: StandalonePaymentCancelResponse schema from Adyen API
layout: schema
name: StandalonePaymentCancelResponse
properties_list:
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: The [`reference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference) of the payment to cancel.
  name: paymentReference
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
schema_file: json-schema/checkout-standalone-payment-cancel-response-schema.json
slug: checkout-standalone-payment-cancel-response
tags:
- Payments
- Financial Services
- Fintech
title: StandalonePaymentCancelResponse
---
