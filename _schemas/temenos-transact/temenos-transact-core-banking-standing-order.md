---
description: A standing order instruction for recurring payments
layout: schema
name: StandingOrder
properties_list:
- description: Unique standing order identifier
  name: standingOrderId
  type: string
- description: Debit account identifier
  name: accountId
  type: string
- description: Beneficiary identifier
  name: beneficiaryId
  type: string
- description: Beneficiary account identifier
  name: beneficiaryAccountId
  type: string
- description: Name of the beneficiary
  name: beneficiaryName
  type: string
- description: Recurring payment amount
  name: amount
  type: number
- description: Payment currency
  name: currency
  type: string
- description: Payment frequency
  name: frequency
  type: string
- description: Date of the first payment
  name: startDate
  type: string
- description: Date of the last payment (optional for indefinite)
  name: endDate
  type: string
- description: Date of the next scheduled payment
  name: nextPaymentDate
  type: string
- description: Standing order status
  name: status
  type: string
- description: Payment description
  name: narrative
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-standing-order-schema.json
slug: temenos-transact-core-banking-standing-order
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: StandingOrder
---
