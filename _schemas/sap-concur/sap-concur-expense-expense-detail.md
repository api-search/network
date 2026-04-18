---
description: The full representation of an expense entry
layout: schema
name: ExpenseDetail
properties_list:
- description: Unique identifier of the expense
  name: expenseId
  type: string
- description: The date the transaction occurred
  name: transactionDate
  type: string
- description: Business justification, maximum 64 characters
  name: businessPurpose
  type: string
- description: The allocation status of this expense
  name: allocationState
  type: string
- description: Whether this is a non-reimbursable personal expense
  name: isPersonalExpense
  type: boolean
- description: Whether the expense has been rejected by an approver
  name: isExpenseRejected
  type: boolean
- description: Whether a physical receipt has been received
  name: isPaperReceiptReceived
  type: boolean
- description: Whether the expense has policy exceptions
  name: hasExceptions
  type: boolean
- description: Reference to a supplier invoice
  name: invoiceId
  type: string
- description: ''
  name: customData
  type: array
- description: When the expense was last modified (ISO 8601)
  name: lastModifiedDate
  type: string
- description: HATEOAS navigation links
  name: links
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-expense-detail-schema.json
slug: sap-concur-expense-expense-detail
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ExpenseDetail
---
