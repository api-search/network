---
description: A fund transfer operation in Temenos Transact for moving funds between accounts, supporting internal transfers, domestic payments, and cross-border transactions.
layout: schema
name: FundTransfer
properties_list:
- description: Unique transfer identifier
  name: transferId
  type: string
- description: Source account identifier
  name: debitAccountId
  type: string
- description: Currency of the debit account
  name: debitCurrency
  type: string
- description: Destination account identifier
  name: creditAccountId
  type: string
- description: Currency of the credit account
  name: creditCurrency
  type: string
- description: Transfer amount
  name: amount
  type: number
- description: Amount credited (may differ due to exchange rate)
  name: creditAmount
  type: number
- description: Type of transfer
  name: transferType
  type: string
- description: Current transfer status
  name: status
  type: string
- description: Value date of the transfer
  name: valueDate
  type: string
- description: Actual execution date
  name: executionDate
  type: string
- description: Applied exchange rate for cross-currency transfers
  name: exchangeRate
  type: number
- description: Total charges applied
  name: chargesAmount
  type: number
- description: Currency of the charges
  name: chargesCurrency
  type: string
- description: Transfer description or purpose
  name: narrative
  type: string
- description: End-to-end reference for payment tracking
  name: endToEndReference
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-fund-transfer-schema.json
slug: temenos-transact-core-banking-fund-transfer
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: FundTransfer
---
