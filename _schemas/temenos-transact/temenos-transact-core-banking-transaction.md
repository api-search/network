---
description: A financial transaction record in Temenos Transact representing a debit or credit entry against an account.
layout: schema
name: Transaction
properties_list:
- description: Unique transaction identifier
  name: transactionId
  type: string
- description: Account against which the transaction was posted
  name: accountId
  type: string
- description: Type classification of the transaction
  name: transactionType
  type: string
- description: Whether the transaction is a debit or credit
  name: debitOrCredit
  type: string
- description: Transaction amount in account currency
  name: amount
  type: number
- description: Currency of the transaction
  name: currency
  type: string
- description: Date the transaction was booked
  name: bookingDate
  type: string
- description: Value date for interest calculation purposes
  name: valueDate
  type: string
- description: Date the transaction was processed
  name: processingDate
  type: string
- description: Transaction reference number
  name: reference
  type: string
- description: Transaction description or narrative text
  name: narrative
  type: string
- description: Account identifier of the counterparty
  name: counterpartyAccountId
  type: string
- description: Name of the counterparty
  name: counterpartyName
  type: string
- description: Running balance after this transaction
  name: balance
  type: number
- description: Exchange rate applied if currency conversion occurred
  name: exchangeRate
  type: number
- description: Charges applied to this transaction
  name: chargesAmount
  type: number
- description: Whether this transaction is a reversal
  name: reversalIndicator
  type: boolean
- description: Statement number this transaction belongs to
  name: statementNumber
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-transaction-schema.json
slug: temenos-transact-core-banking-transaction
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Transaction
---
