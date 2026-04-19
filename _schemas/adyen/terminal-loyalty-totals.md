---
description: Totals of the loyalty transaction during the reconciliation period.
layout: schema
name: LoyaltyTotals
properties_list:
- description: ''
  name: TransactionType
  type: object
- description: Number of processed transaction during the period.
  name: TransactionCount
  type: integer
- description: Sum of amount of processed transaction during the period.
  name: TransactionAmount
  type: number
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-loyalty-totals-schema.json
slug: terminal-loyalty-totals
tags:
- Payments
- Financial Services
- Fintech
title: LoyaltyTotals
---
