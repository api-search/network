---
description: An aggregated summary of settlement activity for a single disbursement batch from Affirm to the merchant.
layout: schema
name: SettlementEventSummary
properties_list:
- description: A unique identifier for this settlement event summary.
  name: id
  type: string
- description: Total amount disbursed in this batch in the smallest currency unit.
  name: total_amount
  type: integer
- description: ISO 4217 currency code for this disbursement.
  name: currency
  type: string
- description: Number of individual settlement events included in this batch.
  name: event_count
  type: integer
- description: Timestamp when the disbursement was initiated, in RFC 3339 format.
  name: disbursed_at
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/transactions-settlement-event-summary-schema.json
slug: transactions-settlement-event-summary
tags: []
title: SettlementEventSummary
---
