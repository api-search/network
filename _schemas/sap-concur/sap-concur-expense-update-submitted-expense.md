---
description: Limited-field update for an expense on a submitted report. Only accessible with Company JWT authentication.
layout: schema
name: UpdateSubmittedExpense
properties_list:
- description: Business justification, maximum 64 characters
  name: businessPurpose
  type: string
- description: The source system that created or modified the expense
  name: expenseSource
  type: string
- description: Whether to mark the expense as rejected
  name: isExpenseRejected
  type: boolean
- description: Whether a physical receipt has been received
  name: isPaperReceiptReceived
  type: boolean
- description: ''
  name: customData
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-update-submitted-expense-schema.json
slug: sap-concur-expense-update-submitted-expense
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: UpdateSubmittedExpense
---
