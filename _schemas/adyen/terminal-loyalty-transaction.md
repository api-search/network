---
description: LoyaltyTransaction schema from Adyen API
layout: schema
name: LoyaltyTransaction
properties_list:
- description: ''
  name: LoyaltyTransactionType
  type: object
- description: ''
  name: Currency
  type: string
- description: ''
  name: TotalAmount
  type: number
- description: ''
  name: OriginalPOITransaction
  type: object
- description: ''
  name: TransactionConditions
  type: object
- description: ''
  name: SaleItem
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-loyalty-transaction-schema.json
slug: terminal-loyalty-transaction
tags:
- Payments
- Financial Services
- Fintech
title: LoyaltyTransaction
---
