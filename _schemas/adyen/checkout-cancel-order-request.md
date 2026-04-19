---
description: CancelOrderRequest schema from Adyen API
layout: schema
name: CancelOrderRequest
properties_list:
- description: The merchant account identifier that orderData belongs to.
  name: merchantAccount
  type: string
- description: The order request object that contains a pspReference that represents the order and the matching encrypted order data.
  name: order
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-cancel-order-request-schema.json
slug: checkout-cancel-order-request
tags:
- Payments
- Financial Services
- Fintech
title: CancelOrderRequest
---
