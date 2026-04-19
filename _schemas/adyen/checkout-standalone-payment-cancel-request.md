---
description: StandalonePaymentCancelRequest schema from Adyen API
layout: schema
name: StandalonePaymentCancelRequest
properties_list:
- description: Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).
  name: applicationInfo
  type: object
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: The [`reference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference) of the payment that you want to cancel.
  name: paymentReference
  type: string
- description: 'Your reference for the cancel request. Maximum length: 80 characters.'
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-standalone-payment-cancel-request-schema.json
slug: checkout-standalone-payment-cancel-request
tags:
- Payments
- Financial Services
- Fintech
title: StandalonePaymentCancelRequest
---
