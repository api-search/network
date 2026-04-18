---
description: JSON Merge Patch body for updating an unsubmitted report. All fields from NewReport are updatable.
layout: schema
name: UpdateReport
properties_list:
- description: The name or title of the expense report
  name: name
  type: string
- description: The business justification for the expenses
  name: businessPurpose
  type: string
- description: ''
  name: reportDate
  type: string
- description: ''
  name: startDate
  type: string
- description: ''
  name: endDate
  type: string
- description: ''
  name: countryCode
  type: string
- description: ''
  name: countrySubDivisionCode
  type: string
- description: ''
  name: policyId
  type: string
- description: ''
  name: customData
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-update-report-schema.json
slug: sap-concur-expense-update-report
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: UpdateReport
---
