---
description: Represents an Affirm-issued virtual card number (VCN) used in the Affirm Lite integration pattern to process payments through traditional card networks.
layout: schema
name: Card
properties_list:
- description: Unique identifier for this virtual card.
  name: id
  type: string
- description: Checkout session identifier associated with this card.
  name: checkout_id
  type: string
- description: Current status of the virtual card.
  name: status
  type: string
- description: Virtual card number (PAN).
  name: number
  type: string
- description: Card verification value.
  name: cvv
  type: string
- description: Card expiration date in MM/YY format.
  name: expiration
  type: string
- description: Billing address associated with this virtual card.
  name: billing
  type: object
- description: Authorized amount on this virtual card in cents.
  name: amount
  type: integer
- description: ISO 4217 currency code.
  name: currency
  type: string
- description: Card creation timestamp in RFC 3339 format.
  name: created
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/direct-api-card-schema.json
slug: direct-api-card
tags: []
title: Card
---
