---
description: CheckoutAwaitAction schema from Adyen API
layout: schema
name: CheckoutAwaitAction
properties_list:
- description: Encoded payment data.
  name: paymentData
  type: string
- description: Specifies the payment method.
  name: paymentMethodType
  type: string
- description: '**await**'
  name: type
  type: string
- description: Specifies the URL to redirect to.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-await-action-schema.json
slug: checkout-checkout-await-action
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutAwaitAction
---
