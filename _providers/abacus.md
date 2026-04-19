---
api_count: 1
apis:
- description: The Abacus API provides programmatic access to expense management functionality, including inviting and suspending members, listing and retrieving expense reports, and integrating with third-party pla
  name: Abacus API
  slug: abacus-api
capabilities:
- description: 'Unified workflow for managing employee expenses, reimbursements, and member provisioning. Enables finance teams and administrators to automate expense reporting, track spending by member or category, '
  name: Abacus Expense Management
  slug: expense-management
common:
- title: ''
  type: Website
  url: https://www.abacus.com/
- title: ''
  type: Documentation
  url: https://support.abacus.com/hc/en-us/articles/12493681200269-Abacus-API
- title: ''
  type: Support
  url: https://support.abacus.com/
- title: ''
  type: PrivacyPolicy
  url: https://legal.emburse.com/
- title: ''
  type: TrustCenter
  url: https://trust.emburse.com/
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/rules/abacus-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/vocabulary/abacus-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/capabilities/expense-management.yaml
- title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-ld/abacus-api-context.jsonld
created: '2024-01-15'
description: Abacus (now part of Emburse Spend) is an expense management platform that allows businesses to streamline expense reporting, receipts, and reimbursements. The Abacus API is available to partners and enterprise customers, providing programmatic access to member management and expense operations using OAuth 2.0 authentication.
features:
- description: Invite, update, and suspend organization members programmatically
  name: Member Management
- description: Retrieve and filter expense reports by status, member, and date range
  name: Expense Tracking
- description: Secure API access using client credentials grant flow
  name: OAuth 2.0 Authentication
- description: Link receipts to expense reports via URL references
  name: Receipt Management
- description: Categorize expenses across meals, travel, lodging, office supplies, and software
  name: Multi-category Expenses
- description: Paginated API responses with configurable page sizes
  name: Paginated Results
image: /assets/icons/abacus.png
integrations:
- description: Sync expense data with QuickBooks for accounting reconciliation
  name: QuickBooks
- description: Integrate with Xero for automated expense accounting
  name: Xero
- description: Connect expense reports with NetSuite ERP
  name: NetSuite
- description: Sync expenses with Sage Intacct for financial management
  name: Sage Intacct
jsonld:
- class_count: 8
  name: Abacus Api Context
  property_count: 27
  slug: abacus-api-context
layout: provider
modified: '2026-04-19'
name: Abacus
rules:
- name: Abacus API Rules
  rule_count: 39
  severity_counts:
    error: 13
    hint: 0
    info: 7
    warn: 19
  slug: abacus-spectral-rules
skills: []
slug: abacus
solutions: []
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/apis.yml
use_cases:
- description: Automatically invite new employees to the expense platform via API
  name: Employee Onboarding
- description: Programmatically suspend departed employees from expense access
  name: Employee Offboarding
- description: Retrieve and reconcile expense reports for accounting integration
  name: Expense Reconciliation
- description: Pull expense data by category, member, or date range for reporting
  name: Spend Analytics
- description: Connect Abacus expense data with ERP and accounting systems
  name: Third-party Integration
---
