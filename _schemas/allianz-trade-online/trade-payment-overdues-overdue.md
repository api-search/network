---
description: A payment overdue reported to Allianz Trade
layout: schema
name: Overdue
properties_list:
- description: Unique identifier for the payment overdue
  name: overdueId
  type: string
- description: Trade credit insurance policy identifier
  name: policyId
  type: string
- description: Overdue category code (OVD=default, EXP=extension, RES=rescheduling)
  name: overdueCategoryTypeCode
  type: string
- description: Name of the debtor with the payment overdue
  name: debtorName
  type: string
- description: Allianz Trade debtor identifier
  name: debtorId
  type: string
- description: Amount overdue in the policy currency
  name: overdueAmount
  type: number
- description: ISO 4217 currency code
  name: currency
  type: string
- description: Original invoice due date
  name: dueDate
  type: string
- description: Customer invoice reference number
  name: invoiceReference
  type: string
- description: Current status of the overdue report
  name: status
  type: string
- description: Timestamp when the overdue was reported
  name: reportedAt
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-payment-overdues-overdue-schema.json
slug: trade-payment-overdues-overdue
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: Overdue
---
