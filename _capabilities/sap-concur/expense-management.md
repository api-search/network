---
consumed_apis:
- concur-expense
description: Unified expense management workflow combining report creation, expense tracking, approval workflows, and allocation management. Used by finance teams, approvers, and employees to manage the full expense lifecycle.
layout: capability
name: SAP Concur Expense Management
operations:
- description: Create a new expense report.
  method: POST
  name: create-report
  path: /v1/reports
- description: Get reports pending approval.
  method: GET
  name: get-reports-to-approve
  path: /v1/reports
- description: Retrieve a report.
  method: GET
  name: get-report
  path: /v1/reports/{reportId}
- description: Submit for approval.
  method: POST
  name: submit-report
  path: /v1/reports/{reportId}/submit
- description: Approve an expense report.
  method: POST
  name: approve-report
  path: /v1/reports/{reportId}/approve
- description: Get expenses for a report.
  method: GET
  name: get-expenses
  path: /v1/expenses
- description: Get report comments.
  method: GET
  name: get-comments
  path: /v1/comments
- description: Add a report comment.
  method: POST
  name: create-comment
  path: /v1/comments
personas: []
provider_name: SAP Concur
provider_slug: sap-concur
search_terms:
- submit an expense report for approval.
- create a new expense report.
- add a report comment.
- expense entry operations.
- get expenses
- approve report
- update an unsubmitted expense report.
- delete report
- send back report
- get report
- get report comments
- retrieve a report.
- get expenses for a report.
- get reports to approve
- financial services
- add a comment to an expense report.
- get a single expense entry.
- update report
- individual report operations.
- business travel
- retrieve an expense report by id.
- delete an unsubmitted expense report.
- submit report
- get expense entries for a report.
- get comments on an expense report.
- approve an expense report.
- approve report.
- travel management
- get allocations
- report comments.
- invoice management
- get report comments.
- sap concur
- get expense allocations.
- recall report
- approval workflows
- expense report lifecycle management.
- expense management
- get reports pending approval.
- submit report.
- create comment
- create report
- get expense
- recall a submitted expense report.
- send back an expense report for revision.
- create report comment
- submit for approval.
- get comments
- list expense reports pending approval.
slug: expense-management
tags:
- SAP Concur
- Expense Management
- Approval Workflows
- Financial Services
tools:
- description: Create a new expense report.
  hints:
    readOnly: false
  name: create-report
- description: Retrieve an expense report by ID.
  hints:
    idempotent: true
    readOnly: true
  name: get-report
- description: Update an unsubmitted expense report.
  hints:
    idempotent: true
    readOnly: false
  name: update-report
- description: Delete an unsubmitted expense report.
  hints:
    destructive: true
    readOnly: false
  name: delete-report
- description: List expense reports pending approval.
  hints:
    idempotent: true
    readOnly: true
  name: get-reports-to-approve
- description: Submit an expense report for approval.
  hints:
    readOnly: false
  name: submit-report
- description: Approve an expense report.
  hints:
    readOnly: false
  name: approve-report
- description: Send back an expense report for revision.
  hints:
    readOnly: false
  name: send-back-report
- description: Recall a submitted expense report.
  hints:
    readOnly: false
  name: recall-report
- description: Get expense entries for a report.
  hints:
    idempotent: true
    readOnly: true
  name: get-expenses
- description: Get a single expense entry.
  hints:
    idempotent: true
    readOnly: true
  name: get-expense
- description: Get expense allocations.
  hints:
    idempotent: true
    readOnly: true
  name: get-allocations
- description: Get comments on an expense report.
  hints:
    idempotent: true
    readOnly: true
  name: get-report-comments
- description: Add a comment to an expense report.
  hints:
    readOnly: false
  name: create-report-comment
---
