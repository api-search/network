---
description: A summary of an expense entry on a report
layout: schema
name: ExpenseSummary
properties_list:
- description: Unique identifier of the expense
  name: expenseId
  type: string
- description: The date the transaction occurred
  name: transactionDate
  type: string
- description: Business justification for this expense
  name: businessPurpose
  type: string
- description: ''
  name: links
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-expense-summary-schema.json
slug: sap-concur-expense-expense-summary
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ExpenseSummary
---
