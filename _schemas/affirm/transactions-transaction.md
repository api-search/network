---
description: Represents an Affirm payment transaction, capturing the full lifecycle from authorization through capture, refund, and void operations.
layout: schema
name: Transaction
properties_list:
- description: A unique identifier representing the transaction.
  name: id
  type: string
- description: A unique identifier referencing the Checkout object that originated this transaction.
  name: checkout_id
  type: string
- description: Identifies the order within the merchant's order management system.
  name: order_id
  type: string
- description: Current state of the transaction.
  name: status
  type: string
- description: The original amount financed to the customer in this transaction, expressed in the smallest currency unit (e.g., cents for USD).
  name: amount
  type: integer
- description: The cumulative amount refunded back to the customer from this transaction, expressed in the smallest currency unit.
  name: amount_refunded
  type: integer
- description: Local transaction currency following ISO 4217 standards.
  name: currency
  type: string
- description: The time when the transaction was created, in RFC 3339 format.
  name: created
  type: string
- description: The time when the transaction authorization expires and can no longer be captured, in RFC 3339 format.
  name: authorization_expiration
  type: string
- description: A unique identifier of the provider financing the transaction.
  name: provider_id
  type: integer
- description: Indicates whether tax was paid by the provider (applicable to Affirm Connect only).
  name: remove_tax
  type: boolean
- description: Array of TransactionEvent objects documenting the transaction history.
  name: events
  type: array
- description: A JWT signing the JSON response. If PII is included, this token is also encrypted.
  name: token
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/transactions-transaction-schema.json
slug: transactions-transaction
tags: []
title: Transaction
---
