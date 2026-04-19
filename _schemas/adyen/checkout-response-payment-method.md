---
description: ResponsePaymentMethod schema from Adyen API
layout: schema
name: ResponsePaymentMethod
properties_list:
- description: The card brand that the shopper used to pay. Only returned if `paymentMethod.type` is **scheme**.
  name: brand
  type: string
- description: The `paymentMethod.type` value used in the request.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-response-payment-method-schema.json
slug: checkout-response-payment-method
tags:
- Payments
- Financial Services
- Fintech
title: ResponsePaymentMethod
---
