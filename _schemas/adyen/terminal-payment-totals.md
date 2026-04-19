---
description: Totals of the payment transaction during the reconciliation period.
layout: schema
name: PaymentTotals
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
schema_file: json-schema/terminal-payment-totals-schema.json
slug: terminal-payment-totals
tags:
- Payments
- Financial Services
- Fintech
title: PaymentTotals
---
