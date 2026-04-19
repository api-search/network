---
description: Represents an Affirm checkout session containing all order details, customer information, and merchant configuration required to initiate the Affirm buy now pay later financing flow. Checkout objects are created via the Checkout API and result in a checkout token that is exchanged for a transaction authorization after customer confirmation.
layout: schema
name: Affirm Checkout
properties_list:
- description: Unique identifier assigned to this checkout session by Affirm.
  name: checkout_id
  type: string
- description: Current status of the checkout session.
  name: checkout_status
  type: string
- description: The checkout flow type used for this session (e.g., classic, direct).
  name: checkout_flow_type
  type: string
- description: ''
  name: merchant
  type: object
- description: ''
  name: shipping
  type: object
- description: ''
  name: billing
  type: object
- description: ''
  name: store
  type: object
- description: Array of item objects representing the products being purchased in this checkout.
  name: items
  type: array
- description: Map of discount codes to discount objects applied to this checkout.
  name: discounts
  type: object
- description: Arbitrary key-value metadata for merchant tracking. All values must be strings.
  name: metadata
  type: object
- description: The merchant's internal order identifier stored for future reference and reconciliation.
  name: order_id
  type: string
- description: Three-letter ISO 4217 currency code in uppercase.
  name: currency
  type: string
- description: A financing program code applied to this checkout that determines the loan terms presented to the customer.
  name: financing_program
  type: string
- description: Internal financing program identifier applied to this checkout.
  name: financial_program_name
  type: string
- description: Customer-facing financing program name.
  name: financial_program_external_name
  type: string
- description: The total shipping amount in cents.
  name: shipping_amount
  type: integer
- description: The total tax amount in cents.
  name: tax_amount
  type: integer
- description: The total amount of the checkout in the smallest currency unit (cents for USD/CAD, pence for GBP).
  name: total
  type: integer
- description: ISO 8601 timestamp specifying when the checkout session expires.
  name: checkout_expiration
  type: string
- description: Time-to-live deadline by which the customer must confirm the checkout.
  name: expiration_time
  type: string
- description: Loan billing frequency for the financing applied to this checkout.
  name: billing_frequency
  type: string
- description: Version of the Affirm API used to create this checkout.
  name: api_version
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/affirm-checkout-schema.json
slug: affirm-checkout
tags: []
title: Affirm Checkout
---
