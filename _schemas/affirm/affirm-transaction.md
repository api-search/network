---
description: Represents an Affirm payment transaction, capturing the full lifecycle from authorization through capture, refund, and void. Transactions are created by exchanging a checkout token via the Transactions API after a customer completes the Affirm checkout flow.
layout: schema
name: Affirm Transaction
properties_list:
- description: A unique identifier representing the transaction, assigned by Affirm upon authorization.
  name: id
  type: string
- description: A unique identifier referencing the Checkout object that originated this transaction.
  name: checkout_id
  type: string
- description: Identifies the order within the merchant's order management system, used for reconciliation.
  name: order_id
  type: string
- description: Current lifecycle state of the transaction.
  name: status
  type: string
- description: The original amount financed to the customer, expressed in the smallest currency unit (e.g., cents for USD).
  name: amount
  type: integer
- description: The cumulative amount refunded to the customer from this transaction, in the smallest currency unit.
  name: amount_refunded
  type: integer
- description: The ISO 4217 currency code for this transaction.
  name: currency
  type: string
- description: The timestamp when the transaction was created, in RFC 3339 format.
  name: created
  type: string
- description: The timestamp after which the transaction authorization expires and can no longer be captured, in RFC 3339 format.
  name: authorization_expiration
  type: string
- description: A unique identifier of the financing provider for this transaction.
  name: provider_id
  type: integer
- description: Indicates whether tax was paid by the financing provider. Applicable to Affirm Connect integrations only.
  name: remove_tax
  type: boolean
- description: Array of TransactionEvent objects documenting the full history of actions taken on this transaction.
  name: events
  type: array
- description: A JWT signing the JSON response body. When PII is included in the response, this token is also encrypted.
  name: token
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/affirm-transaction-schema.json
slug: affirm-transaction
tags: []
title: Affirm Transaction
---
