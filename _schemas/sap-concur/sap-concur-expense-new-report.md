---
description: Request body for creating a new expense report
layout: schema
name: NewReport
properties_list:
- description: The name or title of the expense report
  name: name
  type: string
- description: The business justification for the expenses
  name: businessPurpose
  type: string
- description: The date of the report (YYYY-MM-DD)
  name: reportDate
  type: string
- description: The start date of the reporting period
  name: startDate
  type: string
- description: The end date of the reporting period
  name: endDate
  type: string
- description: ISO 4217 three-letter currency code for the report
  name: currencyCode
  type: string
- description: ISO 3166-1 alpha-2 country code
  name: countryCode
  type: string
- description: ISO 3166-2 subdivision code (state/province)
  name: countrySubDivisionCode
  type: string
- description: The identifier of the expense policy to apply
  name: policyId
  type: string
- description: Custom field values for the report header
  name: customData
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-new-report-schema.json
slug: sap-concur-expense-new-report
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: NewReport
---
