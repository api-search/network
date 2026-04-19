---
description: Request body for creating or updating an Affirm checkout session, containing all order and customer information required to initiate the Affirm financing flow.
layout: schema
name: CheckoutRequest
properties_list:
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
- description: A map of discount codes to discount objects. Each key is the discount code and each value contains the discount amount and name.
  name: discounts
  type: object
- description: Arbitrary key-value metadata for merchant tracking. Values must be strings.
  name: metadata
  type: object
- description: The merchant's internal order identifier. Stored for future reference and reconciliation.
  name: order_id
  type: string
- description: Three-letter ISO 4217 currency code in uppercase. Supported values are USD, CAD, and GBP.
  name: currency
  type: string
- description: Financing program code to apply to this checkout, if applicable. Determines the available loan terms presented to the customer.
  name: financing_program
  type: string
- description: The total shipping amount in cents.
  name: shipping_amount
  type: integer
- description: The total tax amount in cents.
  name: tax_amount
  type: integer
- description: The total amount of the checkout in cents (USD, CAD) or pence (GBP).
  name: total
  type: integer
- description: ISO 8601 timestamp specifying when the checkout session expires.
  name: checkout_expiration
  type: string
- description: Time-to-live deadline by which the customer must confirm the checkout.
  name: expiration_time
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/checkout-checkout-request-schema.json
slug: checkout-checkout-request
tags: []
title: CheckoutRequest
---
