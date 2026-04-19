---
description: Represents a single event in the lifecycle of a transaction, such as an authorization, capture, refund, or void.
layout: schema
name: TransactionEvent
properties_list:
- description: A unique identifier for the transaction event.
  name: id
  type: string
- description: The type of transaction event.
  name: type
  type: string
- description: The amount associated with this event in the smallest currency unit.
  name: amount
  type: integer
- description: The ISO 4217 currency code for this event.
  name: currency
  type: string
- description: The fee charged by Affirm for this event in the smallest currency unit.
  name: fee
  type: integer
- description: The time when this event was created, in RFC 3339 format.
  name: created
  type: string
- description: An external reference identifier associated with this event.
  name: reference_id
  type: string
- description: Additional key-value metadata associated with this event for merchant tracking purposes.
  name: metadata
  type: object
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/transactions-transaction-event-schema.json
slug: transactions-transaction-event
tags: []
title: TransactionEvent
---
