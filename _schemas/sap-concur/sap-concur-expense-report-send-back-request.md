---
description: Request body for sending a report back to the submitter
layout: schema
name: ReportSendBackRequest
properties_list:
- description: Explanation of why the report is being returned for corrections
  name: comment
  type: string
- description: The expected current workflow step code
  name: expectedStepCode
  type: string
- description: The expected current workflow step sequence number
  name: expectedStepSequence
  type: integer
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-report-send-back-request-schema.json
slug: sap-concur-expense-report-send-back-request
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ReportSendBackRequest
---
