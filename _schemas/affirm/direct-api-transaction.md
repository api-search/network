---
description: Represents an Affirm payment transaction at any point in its lifecycle.
layout: schema
name: Transaction
properties_list:
- description: Unique identifier for this transaction.
  name: id
  type: string
- description: Identifier of the checkout session that originated this transaction.
  name: checkout_id
  type: string
- description: Merchant's internal order identifier.
  name: order_id
  type: string
- description: Current lifecycle status of the transaction.
  name: status
  type: string
- description: Original authorized amount in cents.
  name: amount
  type: integer
- description: Cumulative amount refunded in cents.
  name: amount_refunded
  type: integer
- description: ISO 4217 currency code.
  name: currency
  type: string
- description: Creation timestamp in RFC 3339 format.
  name: created
  type: string
- description: Timestamp after which the authorization can no longer be captured.
  name: authorization_expiration
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/direct-api-transaction-schema.json
slug: direct-api-transaction
tags: []
title: Transaction
---
