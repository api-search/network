---
description: Represents an Affirm checkout session with full order details, customer information, and current checkout status.
layout: schema
name: Checkout
properties_list:
- description: Unique identifier for this checkout session.
  name: checkout_id
  type: string
- description: Current status of the checkout session.
  name: checkout_status
  type: string
- description: The checkout flow type used for this session.
  name: checkout_flow_type
  type: string
- description: ISO 4217 currency code for the checkout.
  name: currency
  type: string
- description: Total checkout amount in cents.
  name: total
  type: integer
- description: Shipping cost in cents.
  name: shipping_amount
  type: integer
- description: Tax amount in cents.
  name: tax_amount
  type: integer
- description: Merchant's internal order identifier.
  name: order_id
  type: string
- description: Internal financing program identifier applied to this checkout.
  name: financial_program_name
  type: string
- description: Customer-facing financing program name.
  name: financial_program_external_name
  type: string
- description: Loan billing frequency for the financing applied.
  name: billing_frequency
  type: string
- description: Version of the Affirm API used to create this checkout.
  name: api_version
  type: string
- description: Product category associated with this checkout, if set.
  name: product_type
  type: string
- description: ''
  name: billing
  type: object
- description: ''
  name: shipping
  type: object
- description: ''
  name: merchant
  type: object
- description: Additional checkout metadata.
  name: metadata
  type: object
- description: Affirm internal tracking information.
  name: meta
  type: object
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/checkout-checkout-schema.json
slug: checkout-checkout
tags: []
title: Checkout
---
