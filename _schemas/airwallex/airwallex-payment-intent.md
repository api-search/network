---
description: An Airwallex payment intent representing a payment session for collecting customer payment.
layout: schema
name: PaymentIntent
properties_list:
- description: Unique payment intent identifier.
  name: id
  type: string
- description: Payment amount in the specified currency.
  name: amount
  type: number
- description: ISO 4217 currency code.
  name: currency
  type: string
- description: Merchant's own order identifier.
  name: merchant_order_id
  type: string
- description: Current payment intent status.
  name: status
  type: string
- description: Client secret for frontend SDK initialization.
  name: client_secret
  type: string
- description: Amount captured so far.
  name: captured_amount
  type: number
- description: Airwallex customer ID.
  name: customer_id
  type: string
- description: Payment method configuration options.
  name: payment_method_options
  type: object
- description: Statement descriptor shown on customer bank statement.
  name: descriptor
  type: string
- description: Arbitrary key-value metadata for the payment intent.
  name: metadata
  type: object
- description: Timestamp when the payment intent was created.
  name: created_at
  type: string
- description: Timestamp of last update.
  name: updated_at
  type: string
provider_name: Airwallex
provider_slug: airwallex
schema_file: json-schema/airwallex-payment-intent-schema.json
slug: airwallex-payment-intent
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
title: PaymentIntent
---
