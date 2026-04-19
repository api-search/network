---
description: PaymentReversalRequest schema from Adyen API
layout: schema
name: PaymentReversalRequest
properties_list:
- description: Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).
  name: applicationInfo
  type: object
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: 'Your reference for the reversal request. Maximum length: 80 characters.'
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-reversal-request-schema.json
slug: checkout-payment-reversal-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentReversalRequest
---
