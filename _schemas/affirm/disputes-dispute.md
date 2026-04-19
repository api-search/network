---
description: Represents a payment dispute filed by a customer against an Affirm transaction, including its current status, reason, and any evidence submitted by the merchant.
layout: schema
name: Dispute
properties_list:
- description: Unique identifier for this dispute.
  name: id
  type: string
- description: The identifier of the Affirm transaction being disputed.
  name: transaction_id
  type: string
- description: The identifier of the charge associated with this dispute.
  name: charge_id
  type: string
- description: Current status of the dispute.
  name: status
  type: string
- description: Standardized reason code categorizing the nature of the dispute (e.g., item_not_received, item_not_as_described, unauthorized).
  name: reason_code
  type: string
- description: The disputed amount in cents.
  name: amount
  type: integer
- description: ISO 4217 currency code for the disputed amount.
  name: currency
  type: string
- description: Timestamp when this dispute was created, in RFC 3339 format.
  name: created
  type: string
- description: Deadline by which the merchant must submit evidence to contest this dispute, in RFC 3339 format.
  name: evidence_due_by
  type: string
- description: Timestamp when this dispute was closed, if applicable.
  name: closed_at
  type: string
- description: Final outcome of the dispute after review. Only set when status is won or lost.
  name: outcome
  type: string
- description: List of evidence items submitted by the merchant for this dispute.
  name: evidence
  type: array
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/disputes-dispute-schema.json
slug: disputes-dispute
tags: []
title: Dispute
---
