---
description: Limited-field JSON Merge Patch for updating a submitted report. Only accessible with Company JWT authentication.
layout: schema
name: UpdateSubmittedReport
properties_list:
- description: The name or title of the expense report
  name: name
  type: string
- description: The business justification
  name: businessPurpose
  type: string
- description: A comment to accompany the update
  name: comment
  type: string
- description: Whether physical receipts have been received
  name: isPaperReceiptsReceived
  type: boolean
- description: ''
  name: customData
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-update-submitted-report-schema.json
slug: sap-concur-expense-update-submitted-report
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: UpdateSubmittedReport
---
