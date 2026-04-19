---
description: An insurance claim filed with Allianz Trade
layout: schema
name: Claim
properties_list:
- description: Unique identifier for the insurance claim
  name: claimId
  type: string
- description: Trade credit insurance policy identifier
  name: policyId
  type: string
- description: Name of the debtor who defaulted on payment
  name: debtorName
  type: string
- description: Allianz Trade debtor identifier
  name: debtorId
  type: string
- description: Total amount claimed
  name: claimAmount
  type: number
- description: Amount approved by Allianz Trade (after processing)
  name: approvedAmount
  type: number
- description: ISO 4217 currency code
  name: currency
  type: string
- description: Current status of the claim
  name: claimStatus
  type: string
- description: Date when the financial loss occurred
  name: lossDate
  type: string
- description: Customer invoice reference number
  name: invoiceReference
  type: string
- description: Related payment overdue identifier
  name: overdueId
  type: string
- description: Timestamp when the claim was submitted
  name: submittedAt
  type: string
- description: Timestamp when the claim was resolved
  name: resolvedAt
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-claims-claim-schema.json
slug: trade-claims-claim
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: Claim
---
