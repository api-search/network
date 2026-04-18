---
api_count: 8
apis:
- description: Intuit APIs provide developers with access to a wide range of services and functionalities to help them build innovative solutions for financial management, accounting, and tax-related needs. These AP
  name: Intuit APIs
  slug: intuit
- description: The QuickBooks Online Accounting API is a RESTful API that provides programmatic access to QuickBooks Online company data, including customers, invoices, payments, bills, vendors, accounts, and report
  name: QuickBooks Online Accounting API
  slug: quickbooks-accounting
- description: The QuickBooks Payments API enables developers to process credit card charges, bank account debits (ACH), and manage payment methods within the QuickBooks ecosystem. It supports tokenized card storage
  name: QuickBooks Payments API
  slug: quickbooks-payments
- description: The QuickBooks Payroll and Time API provides programmatic access to payroll and time-tracking data within QuickBooks Online. It supports use cases including time entry management, payroll compensation
  name: QuickBooks Payroll and Time API
  slug: quickbooks-payroll-time
- description: 'The QuickBooks Desktop API allows developers to integrate with QuickBooks Desktop applications using qbXML messages. It provides capabilities for adding, querying, modifying, and deleting data across '
  name: QuickBooks Desktop API
  slug: quickbooks-desktop
- description: The QuickBooks Projects API is a premium API that provides programmatic access to project data within QuickBooks Online Plus, Advanced, Accountant, and Intuit Enterprise Suite. It enables developers t
  name: QuickBooks Projects API
  slug: quickbooks-projects
- description: The QuickBooks Custom Fields API is a premium API that provides programmatic access to custom field definitions and values in QuickBooks Online and Intuit Enterprise Suite. It allows developers to cre
  name: QuickBooks Custom Fields API
  slug: quickbooks-custom-fields
- description: The QuickBooks Sales Tax API is a premium API that provides programmatic access to the automated sales tax calculation capabilities within QuickBooks Online. It enables developers to leverage QuickBoo
  name: QuickBooks Sales Tax API
  slug: quickbooks-sales-tax
asyncapis:
- description: QuickBooks Online Webhooks provide near real-time notifications when data changes in a QuickBooks Online company. When an entity is created, updated, merged, deleted, or voided, Intuit sends an HTTP P
  name: QuickBooks Online Webhooks
  slug: quickbooks-webhooks
capabilities:
- description: Unified workflow for small business accounting automation combining QuickBooks Online invoice, customer, item, and payment management. Used by accountants, bookkeepers, and business owners to automate
  name: Intuit Accounting and Payments
  slug: accounting-and-payments
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.intuit.com
- title: ''
  type: SignUp
  url: https://developer.intuit.com/app/developer/appcard/overview
- title: ''
  type: Blog
  url: https://developer.intuit.com/app/developer/blog
- title: ''
  type: Support
  url: https://help.developer.intuit.com
- title: ''
  type: StatusPage
  url: https://status.developer.intuit.com
- title: ''
  type: TermsOfService
  url: https://developer.intuit.com/app/developer/qbo/docs/learn/terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://www.intuit.com/privacy/
- title: ''
  type: Authentication
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0
- title: ''
  type: Sandbox
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/postman
- title: ''
  type: Console
  url: https://developer.intuit.com/app/developer/qbo/docs/get-started/get-started-with-the-api-explorer
- title: ''
  type: FAQ
  url: https://developer.intuit.com/app/developer/qbo/docs/get-started/partner-faq
- title: ''
  type: GitHubOrganization
  url: https://github.com/intuit
- title: ''
  type: GitHubOrganization
  url: https://github.com/intuitdeveloper
- title: PHP SDK
  type: SDK
  url: https://github.com/intuit/QuickBooks-V3-PHP-SDK
- title: .NET SDK
  type: SDK
  url: https://github.com/intuit/QuickBooks-V3-DotNET-SDK
- title: Java SDK
  type: SDK
  url: https://github.com/intuit/QuickBooks-V3-Java-SDK
- title: Ruby SDK
  type: SDK
  url: https://github.com/intuit/oauth-rubyclient
- title: Node.js SDK
  type: SDK
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections/nodejs
- title: Python SDK
  type: SDK
  url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections/python
- title: ''
  type: ChangeLog
  url: https://blogs.intuit.com/
- title: ''
  type: ReleaseNotes
  url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/platform-release-notes
- title: ''
  type: ReleaseNotes
  url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/general-release-notes
- title: ''
  type: Versioning
  url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions
- title: ''
  type: RateLimits
  url: https://help.developer.intuit.com/s/article/API-call-limits-and-throttling
- title: ''
  type: Security
  url: https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app/security-requirements
- title: ''
  type: Marketplace
  url: https://quickbooks.intuit.com/app/apps/home/en-global/
- title: ''
  type: X
  url: https://x.com/IntuitDev
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intuit-developer
created: '2025-03-01'
description: Collection of APIs offered by Intuit for financial and business management services.
features:
- description: Secure API access using OAuth 2.0 authorization with OpenID Connect for user identity verification.
  name: OAuth 2.0 Authentication
- description: Real-time event notifications for changes to QuickBooks entities including invoices, payments, and customers.
  name: Webhooks
- description: Backward-compatible API versioning allowing access to newer fields and behaviors without breaking existing integrations.
  name: Minor Versioning
- description: Full-featured sandbox environment for testing and development with sample company data.
  name: Sandbox Environment
- description: Support for transactions in multiple currencies with automatic exchange rate management.
  name: Multi-Currency Support
- description: Extensible metadata system allowing up to 12 custom fields across transaction types.
  name: Custom Fields
image: https://developer.intuit.com/app/developer/common/imgs/IntuitDev_Logo.svg
integrations:
- description: Sync e-commerce orders, inventory, and payments between Shopify stores and QuickBooks for automated bookkeeping.
  name: Shopify
- description: Reconcile Stripe payment transactions with QuickBooks invoices and accounts receivable.
  name: Stripe
- description: Import Square POS transactions into QuickBooks for unified financial management.
  name: Square
- description: Connect CRM data with accounting to automate invoice creation from deals and track payment status.
  name: HubSpot
- description: Sync customer and opportunity data between Salesforce CRM and QuickBooks accounting.
  name: Salesforce
jsonld:
- class_count: 0
  name: Intuit Context
  property_count: 8
  slug: intuit-context
- class_count: 0
  name: Quickbooks Accounting Context
  property_count: 0
  slug: quickbooks-accounting-context
layout: provider
modified: '2026-04-18'
name: Intuit
rules:
- name: Intuit API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: intuit-spectral-rules
skills: []
slug: intuit
solutions: []
tags:
- Accounting
- Custom Fields
- Financial
- Financial Services
- Invoicing
- Payments
- Payroll
- Project Management
- Sales Tax
- Small Business
- Tax
- Tax Preparation
- Taxes
- Time Tracking
url: https://raw.githubusercontent.com/api-evangelist/intuit/refs/heads/main/apis.yml
use_cases:
- description: Automate bookkeeping workflows by syncing invoices, payments, and expenses between business systems and QuickBooks.
  name: Accounting Automation
- description: Process credit card and ACH payments linked to QuickBooks invoices for seamless financial reconciliation.
  name: Payment Processing
- description: Integrate payroll and time-tracking data to streamline employee compensation and workforce management.
  name: Payroll Integration
- description: Automate sales tax calculations and ensure tax compliance across different jurisdictions.
  name: Tax Compliance
- description: Build custom financial reports and dashboards by querying QuickBooks accounting data programmatically.
  name: Financial Reporting
---
