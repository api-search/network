---
description: An expense report containing expense entries.
layout: schema
name: ExpenseReport
properties_list:
- description: Unique identifier for the expense report.
  name: reportId
  type: string
- description: Name of the expense report.
  name: reportName
  type: string
- description: Full name of the report owner.
  name: ownerName
  type: string
- description: Business purpose for the expenses.
  name: businessPurpose
  type: string
- description: Date the report was submitted.
  name: submitDate
  type: string
- description: ''
  name: approvalStatus
  type: string
- description: Total amount of all expenses.
  name: total
  type: number
- description: ISO 4217 currency code.
  name: currencyCode
  type: string
- description: ISO country code.
  name: countryCode
  type: string
- description: Date of the report.
  name: reportDate
  type: string
provider_name: SAP Concur
provider_slug: concur
schema_file: json-schema/concur-expense-api-expense-report-schema.json
slug: concur-expense-api-expense-report
tags:
- Expense Management
- Finance
- Invoice
- SAP
- Travel
title: ExpenseReport
---
