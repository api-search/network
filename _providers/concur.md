---
api_count: 8
apis:
- description: REST API for managing expense reports, entries, allocations, and attendees. Supports creating, updating, and submitting expense reports with receipt images, policy validation, and approval workflows.
  name: SAP Concur Expense API
  slug: expense-api
- description: REST API for managing travel itineraries, bookings, and travel profiles. Supports searching for travel options, creating bookings, and managing travel policies and preferences.
  name: SAP Concur Travel API
  slug: travel-api
- description: REST API for accounts payable invoice processing including purchase requests, vendor management, payment batches, and invoice approval workflows.
  name: SAP Concur Invoice API
  slug: invoice-api
- description: REST API for submitting and managing digital receipts from e-commerce providers, ground transportation, hotels, and other merchants directly to Concur expense.
  name: SAP Concur Receipts API
  slug: receipts-api
- description: REST API for managing pre-trip travel requests and approvals, enabling employees to submit travel requests for authorization before booking.
  name: SAP Concur Request API
  slug: request-api
- description: SCIM 2.0-compliant API for provisioning and managing Concur user accounts, roles, and profile information with support for bulk operations.
  name: SAP Concur User Provisioning API
  slug: user-provisioning-api
- description: Event subscription API enabling applications to receive real-time notifications when events occur in Concur such as expense report submissions, approvals, and status changes.
  name: SAP Concur Events API
  slug: events-api
- description: REST API for managing custom lists and list items used in expense forms, travel policies, and invoice configurations for dropdown and lookup fields.
  name: SAP Concur Lists API
  slug: lists-api
capabilities:
- description: Unified spend management workflow combining expense, travel, and invoice APIs for finance teams managing employee spend.
  name: SAP Concur Spend Management
  slug: spend-management
common:
- title: ''
  type: Portal
  url: https://developer.concur.com/
- title: ''
  type: Documentation
  url: https://developer.concur.com/api-reference/
- title: ''
  type: GettingStarted
  url: https://developer.concur.com/api-reference/getting-started.html
- title: ''
  type: Authentication
  url: https://developer.concur.com/api-reference/authentication/apidoc.html
- title: ''
  type: Blog
  url: https://www.concur.com/blog
- title: ''
  type: GitHubOrganization
  url: https://github.com/SAP/concur-platform
- title: ''
  type: Support
  url: https://developer.concur.com/tools-support/support.html
- title: ''
  type: TermsOfService
  url: https://www.concur.com/en-us/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://www.concur.com/en-us/privacy-policy
- title: ''
  type: Sandbox
  url: https://developer.concur.com/manage-apps/register.html
- title: ''
  type: ChangeLog
  url: https://developer.concur.com/tools-support/release-notes/
- title: ''
  type: Pricing
  url: https://www.concur.com/en-us/pricing
created: '2024-01-01'
description: SAP Concur provides a comprehensive suite of REST APIs for travel, expense, and invoice management. The Concur API platform enables integration with expense reporting, travel booking, invoice processing, receipt capture, and user management services used by enterprises worldwide for spend management automation.
features:
- description: Create, submit, and manage expense reports with policy validation and multi-level approval workflows.
  name: Expense Report Management
- description: Capture and process digital receipts from merchants for automatic expense matching.
  name: Receipt Digitization
- description: Search and book travel through API-connected travel management companies and booking tools.
  name: Travel Booking Integration
- description: Automate accounts payable workflows with purchase requests, vendor management, and payment processing.
  name: Invoice Processing
- description: Real-time event subscriptions for expense, travel, and invoice status changes.
  name: Event Notifications
- description: Standards-based user provisioning and management with SCIM 2.0 protocol support.
  name: SCIM User Provisioning
image: /assets/icons/concur.png
integrations:
- description: Financial posting integration for automated expense and invoice data transfer to SAP ERP.
  name: SAP S/4HANA
- description: HR integration for employee data synchronization and travel policy assignment.
  name: SAP SuccessFactors
- description: Automated ride receipt submission from Uber business accounts to Concur expense.
  name: Uber for Business
- description: Ground transportation receipt integration for business ride expense automation.
  name: Lyft
- description: Approval and notification integration for expense workflows within Teams.
  name: Microsoft Teams
jsonld:
- class_count: 2
  name: Concur Context
  property_count: 15
  slug: concur-context
layout: provider
modified: '2026-04-18'
name: SAP Concur
rules:
- name: SAP Concur API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: concur-spectral-rules
skills: []
slug: concur
solutions: []
tags:
- Expense Management
- Finance
- Invoice
- SAP
- Travel
url: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/apis.yml
use_cases:
- description: Integrate Concur expense and invoice data with ERP systems for automated financial posting.
  name: ERP Integration
- description: Build travel booking integrations connecting corporate travel policies with booking engines.
  name: Travel Management
- description: Automatically capture and match digital receipts from e-commerce and travel merchants.
  name: Receipt Automation
- description: Extract expense and travel data for spend analytics, compliance reporting, and budget tracking.
  name: Spend Analytics
- description: Automate Concur user provisioning as part of employee onboarding workflows.
  name: Employee Onboarding
---
