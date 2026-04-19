---
description: CancelOrderResponse schema from Adyen API
layout: schema
name: CancelOrderResponse
properties_list:
- description: A unique reference of the cancellation request.
  name: pspReference
  type: string
- description: 'The result of the cancellation request. Possible values: * **Received** – Indicates the cancellation has successfully been received by Adyen, and will be processed.'
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-cancel-order-response-schema.json
slug: checkout-cancel-order-response
tags:
- Payments
- Financial Services
- Fintech
title: CancelOrderResponse
---
