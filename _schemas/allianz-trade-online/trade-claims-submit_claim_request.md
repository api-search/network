---
description: Request body for submitting an insurance claim
layout: schema
name: SubmitClaimRequest
properties_list:
- description: Trade credit insurance policy identifier
  name: policyId
  type: string
- description: Name of the defaulting debtor
  name: debtorName
  type: string
- description: Allianz Trade debtor identifier
  name: debtorId
  type: string
- description: Total amount to claim
  name: claimAmount
  type: number
- description: ISO 4217 currency code
  name: currency
  type: string
- description: Date when the financial loss occurred
  name: lossDate
  type: string
- description: Customer invoice reference
  name: invoiceReference
  type: string
- description: Related payment overdue identifier
  name: overdueId
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-claims-submit_claim_request-schema.json
slug: trade-claims-submit_claim_request
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: SubmitClaimRequest
---
