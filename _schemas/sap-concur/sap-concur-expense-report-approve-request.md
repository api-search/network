---
description: Request body for approving or recalling a report
layout: schema
name: ReportApproveRequest
properties_list:
- description: An optional comment accompanying the approval
  name: comment
  type: string
- description: Comment explaining why specific expenses are being rejected within an otherwise approved report
  name: expenseRejectedComment
  type: string
- description: Target status identifier
  name: statusId
  type: string
- description: The expected current workflow step code for optimistic concurrency control
  name: expectedStepCode
  type: string
- description: The expected current workflow step sequence number for optimistic concurrency control
  name: expectedStepSequence
  type: integer
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-report-approve-request-schema.json
slug: sap-concur-expense-report-approve-request
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ReportApproveRequest
---
