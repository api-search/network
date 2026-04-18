---
description: A summary of an expense report awaiting approval
layout: schema
name: ReportToApprove
properties_list:
- description: Unique identifier of the report
  name: reportId
  type: string
- description: The report name
  name: name
  type: string
- description: The report owner's user ID
  name: userId
  type: string
- description: Current approval status
  name: approvalStatus
  type: string
- description: When the report was submitted
  name: submitDate
  type: string
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-report-to-approve-schema.json
slug: sap-concur-expense-report-to-approve
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ReportToApprove
---
