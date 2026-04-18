---
description: ''
layout: schema
name: BatchStatusItems
properties_list:
- description: 'The action to be performed on the Digital Payment Application (DPA). The selected action will be applied to all DPAs provided in the items list. __ADD__ - Add DPA __UPDATE__ - Update DPA __DELETE__ - '
  name: action
  type: string
- description: A unique identifier assigned by Mastercard for which tokens are created uniquely for the entity onboarded.
  name: serviceId
  type: string
- description: Token Requestors receive a unique identifier, TRID, which represents the consumer-facing entity name to the Issuer during the tokenization process. This identifier has a one-to-one relationship with t
  name: trid
  type: string
- description: 'The Cardholder facing name of the Merchant. Conditional: Must be supplied when adding Merchants to a Payment Facilitator (PF) program."'
  name: programName
  type: string
- description: Indicates the status of an individual Digital Payment Application (DPA) item in a batch.
  name: status
  type: string
- description: ''
  name: dpaResults
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-batch-status-items-schema.json
slug: mastercard-checkout-solutions-batch-status-items
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: BatchStatusItems
---
