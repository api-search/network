---
description: Represents a single disbursement line item from Affirm to the merchant, associated with a specific transaction event.
layout: schema
name: SettlementEvent
properties_list:
- description: A unique identifier for the settlement event.
  name: id
  type: string
- description: The identifier of the transaction this settlement event belongs to.
  name: transaction_id
  type: string
- description: The identifier of the specific transaction event that triggered this settlement.
  name: transaction_event_id
  type: string
- description: Net disbursement amount in the smallest currency unit.
  name: amount
  type: integer
- description: ISO 4217 currency code for this settlement.
  name: currency
  type: string
- description: Timestamp when this settlement event was created, in RFC 3339 format.
  name: created
  type: string
- description: The type of settlement event corresponding to the transaction action.
  name: type
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/transactions-settlement-event-schema.json
slug: transactions-settlement-event
tags: []
title: SettlementEvent
---
