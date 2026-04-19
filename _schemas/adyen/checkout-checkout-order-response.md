---
description: CheckoutOrderResponse schema from Adyen API
layout: schema
name: CheckoutOrderResponse
properties_list:
- description: The initial amount of the order.
  name: amount
  type: object
- description: The expiry date for the order.
  name: expiresAt
  type: string
- description: The encrypted order data.
  name: orderData
  type: string
- description: The `pspReference` that belongs to the order.
  name: pspReference
  type: string
- description: The merchant reference for the order.
  name: reference
  type: string
- description: The updated remaining amount.
  name: remainingAmount
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-order-response-schema.json
slug: checkout-checkout-order-response
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutOrderResponse
---
