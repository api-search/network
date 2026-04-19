---
description: CreateOrderResponse schema from Adyen API
layout: schema
name: CreateOrderResponse
properties_list:
- description: 'Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**.'
  name: additionalData
  type: object
- description: The initial amount of the order.
  name: amount
  type: object
- description: The date that the order will expire.
  name: expiresAt
  type: string
- description: The fraud result properties of the payment.
  name: fraudResult
  type: object
- description: The encrypted data that will be used by merchant for adding payments to the order.
  name: orderData
  type: string
- description: Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: The reference provided by merchant for creating the order.
  name: reference
  type: string
- description: If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the a
  name: refusalReason
  type: string
- description: The remaining amount in the order.
  name: remainingAmount
  type: object
- description: The result of the order creation request. The value is always **Success**.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-create-order-response-schema.json
slug: checkout-create-order-response
tags:
- Payments
- Financial Services
- Fintech
title: CreateOrderResponse
---
