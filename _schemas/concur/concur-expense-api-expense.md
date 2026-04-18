---
description: An individual expense entry.
layout: schema
name: Expense
properties_list:
- description: Unique identifier for the expense entry.
  name: expenseId
  type: string
- description: Name of the expense type.
  name: expenseTypeName
  type: string
- description: Date of the transaction.
  name: transactionDate
  type: string
- description: Amount of the transaction.
  name: transactionAmount
  type: number
- description: Currency code of the transaction.
  name: transactionCurrencyCode
  type: string
- description: Name of the vendor.
  name: vendorName
  type: string
- description: Description of the expense.
  name: description
  type: string
- description: Whether a receipt is required.
  name: receiptRequired
  type: boolean
provider_name: SAP Concur
provider_slug: concur
schema_file: json-schema/concur-expense-api-expense-schema.json
slug: concur-expense-api-expense
tags:
- Expense Management
- Finance
- Invoice
- SAP
- Travel
title: Expense
---
