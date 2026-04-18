---
description: An itemized line within a parent expense, representing a breakdown of the total amount.
layout: schema
name: ExpenseItemization
properties_list:
- description: Unique identifier of the itemization
  name: itemizationId
  type: string
- description: The parent expense identifier
  name: expenseId
  type: string
- description: The date of the itemized charge
  name: transactionDate
  type: string
- description: Purpose of this specific itemization
  name: businessPurpose
  type: string
- description: ''
  name: customData
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-expense-itemization-schema.json
slug: sap-concur-expense-expense-itemization
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ExpenseItemization
---
