---
description: CreateOrderRequest schema from Adyen API
layout: schema
name: CreateOrderRequest
properties_list:
- description: The total amount of the order.
  name: amount
  type: object
- description: The date that order expires; e.g. 2019-03-23T12:25:28Z. If not provided, the default expiry duration is 1 day.
  name: expiresAt
  type: string
- description: The merchant account identifier, with which you want to process the order.
  name: merchantAccount
  type: string
- description: A custom reference identifying the order.
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-create-order-request-schema.json
slug: checkout-create-order-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateOrderRequest
---
