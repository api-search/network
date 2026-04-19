---
description: Represents a payment dispute filed by a customer against an Affirm transaction. Disputes are managed via the Affirm Disputes API V3, which supports listing disputes, submitting merchant evidence, and closing disputes. Merchants can contest disputes by uploading supporting documentation via the Files API.
layout: schema
name: Affirm Dispute
properties_list:
- description: Unique identifier for this dispute, assigned by Affirm.
  name: id
  type: string
- description: The identifier of the Affirm transaction being disputed.
  name: transaction_id
  type: string
- description: The identifier of the charge associated with this dispute.
  name: charge_id
  type: string
- description: Current lifecycle status of the dispute.
  name: status
  type: string
- description: Standardized reason code categorizing the nature of the customer's dispute claim.
  name: reason_code
  type: string
- description: The disputed amount in the smallest currency unit (e.g., cents for USD).
  name: amount
  type: integer
- description: The ISO 4217 currency code for the disputed amount.
  name: currency
  type: string
- description: Timestamp when this dispute was opened, in RFC 3339 format.
  name: created
  type: string
- description: Deadline by which the merchant must submit evidence to contest this dispute, in RFC 3339 format.
  name: evidence_due_by
  type: string
- description: Timestamp when this dispute was closed, if applicable. Null if still open.
  name: closed_at
  type:
  - string
  - 'null'
- description: Final resolution outcome after dispute review. Only set when status is won or lost.
  name: outcome
  type:
  - string
  - 'null'
- description: List of evidence items submitted by the merchant in response to this dispute.
  name: evidence
  type: array
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/affirm-dispute-schema.json
slug: affirm-dispute
tags: []
title: Affirm Dispute
---
