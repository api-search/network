---
api_count: 31
apis:
- description: Enables integration with Concur Expense for creating, retrieving, and managing expense reports, entries, and related data.
  name: Concur Expense API
  slug: ''
- description: Provides access to travel booking data, profiles, and itinerary information within Concur Travel.
  name: Concur Travel API
  slug: ''
- description: Allows integration with Concur Invoice for managing purchase requests, invoices, and payment requests.
  name: Concur Invoice API
  slug: ''
- description: Enables management of travel requests and approvals within the Concur system.
  name: Concur Request API
  slug: ''
- description: Manages user accounts and profiles, including creating, updating, and retrieving user information. Supports provisioning across Identity, Spend, and Travel services with bulk operations for managing m
  name: Concur User Provisioning API
  slug: ''
- description: Allows for the submission and management of digital receipts within Concur Expense.
  name: Concur Receipt API
  slug: ''
- description: Exposes budget and fiscal year data, enabling partners and clients to read and manage fiscal years, budget categories, budget items, budget tracking fields, and budget adjustments through API endpoint
  name: Concur Budget API
  slug: ''
- description: Provides an automated integration pathway for certified partner financial networks, issuing banks, and fin-tech partners to submit credit card account and transaction data to Concur Expense in near re
  name: Concur Cards API
  slug: ''
- description: Enables the creation of expenses with minimal information such as date, amount, and expense type, with or without a receipt image. Supports attaching receipt files including PNG, PDF, TIFF, and JPEG f
  name: Concur Quick Expense API
  slug: ''
- description: Allows users to create custom exchange rates for a company, supporting bulk uploads of exchange rate data for specified currency pairs and effective dates with a maximum of 100 rates per request.
  name: Concur Exchange Rate API
  slug: ''
- description: Allows an external system to interact with financial documents generated from SAP Concur for financial posting into an ERP, providing an automated solution to request approved expense reports, cash ad
  name: Concur Financial Integration API
  slug: ''
- description: Creates, updates, and reads user core identity profiles following the SCIM 2.0 standard. Enables looking up SAP Concur UUIDs for accessing other v4 APIs for individual users.
  name: Concur Identity API
  slug: ''
- description: Implements the Publish/Subscribe pattern using principles of Event Driven Architecture, notifying clients and partners when specific business events occur such as expense report status changes and tra
  name: Concur Event Subscription Service API
  slug: ''
- description: Allows clients to add interactions with outside systems to their users SAP Concur experience through application connectors, supporting attendee data fetch, list item fetch, event notifications, and e
  name: Concur Callouts API
  slug: ''
- description: Provides a method for custom hotel source suppliers to provide hotel inventory, rates, and booking related functionality to SAP Concur Online Booking Tool, supporting search, rate retrieval, reservati
  name: Concur Direct Connect Hotel Service API
  slug: ''
- description: Enables travel users to access ground transportation inventory from service providers, supporting search, reservation, cancellation, and update operations for ground transportation bookings.
  name: Concur Direct Connect Ground Transportation API
  slug: ''
- description: Facilitates ingestion and retrieval of receipt documents for use within Concur Expense, enabling users to create and retrieve simple receipts by uploading documents with associated metadata.
  name: Concur Spend Documents API
  slug: ''
- description: Provides an automated solution for retrieving, adding, updating, and deleting list items within SAP Concur, supporting hierarchical list structures with parent-child relationships across multiple leve
  name: Concur List Item API
  slug: ''
- description: Enables viewing configured lists within SAP Concur products and creating new lists, supporting shared lists across Expense, Invoice, and Request applications with managed list capabilities for partner
  name: Concur Lists API
  slug: ''
- description: Enables retrieval of travel profile information for specified users and lists of travel profile summaries, available to developers, travel suppliers, and travel management companies.
  name: Concur Travel Profile API
  slug: ''
- description: Allows extraction of travel allowance information from the SAP Concur platform, providing the ability to read travel allowance itinerary data, calculation results, and configuration settings.
  name: Concur Travel Allowance API
  slug: ''
- description: Enables users to create, view, and issue cash advances within Concur Expense. Supports single cash advance creation, retrieval, and issuance operations for both Professional and Standard editions. Req
  name: Concur Cash Advance API
  slug: ''
- description: Gives SAP Concur clients the ability to leverage external data to create and update approved purchase orders. Enables direct connections to manage purchase orders and resolve matching exceptions on in
  name: Concur Purchase Order API
  slug: ''
- description: 'Enables SAP Concur clients to leverage external data to create purchase requests for pre-authorization of purchase orders. Organizations can establish direct connections to automatically generate and '
  name: Concur Purchase Request API
  slug: ''
- description: Provides processes for managing vendor collections used in invoicing, including adding new vendors, updating, retrieving, and deleting information for existing vendors. Supports vendor banking informa
  name: Concur Vendor API
  slug: ''
- description: Enables retrieval and updating of invoices for tax calculation purposes, allowing external tax systems to fetch invoices requiring tax assessment and submit calculated tax amounts and rates back to Co
  name: Concur Sales Tax Validation API
  slug: ''
- description: Manages transmission of compliance documents between SAP Concur and validating vendors, enabling vendors to exchange compliance documents, validate them against relevant authoritative or regulatory so
  name: Concur Document Compliance Gateway API
  slug: ''
- description: Enables clients to manage receipt images attached to expense reports and images associated with invoices. Users can retrieve existing images by report ID, image ID, or invoice ID, and upload new image
  name: Concur Image API
  slug: ''
- description: 'Exposes receipt requests to inform E-Receipt partners which E-Receipts to send to SAP Concur and for which user. Partners receive paginated responses and can filter results using optional timestamps, '
  name: Concur Travel Receipts API
  slug: ''
- description: Retrieves details about locations used by Concur that are valid at a user's company. Supports filtering by name, city, country, and other geographic parameters, and returns location data including IAT
  name: Concur Locations API
  slug: ''
- description: Provides access to the configured attendee types within SAP Concur, allowing retrieval and management of attendee type resources used for categorizing attendees in expense reports.
  name: Concur Expense Attendee Types API
  slug: ''
capabilities:
- description: Unified expense management workflow combining report creation, expense tracking, approval workflows, and allocation management. Used by finance teams, approvers, and employees to manage the full expen
  name: SAP Concur Expense Management
  slug: expense-management
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.concur.com/
- title: ''
  type: Authentication
  url: https://developer.concur.com/api-reference/authentication/getting-started.html
- title: ''
  type: Authentication
  url: https://developer.concur.com/api-reference/authentication/company-auth.html
- title: ''
  type: Support
  url: https://developer.concur.com/support/
- title: ''
  type: TermsOfService
  url: https://www.concur.com/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://www.concur.com/privacy-policy
- title: ''
  type: StatusPage
  url: https://open.concur.com/
- title: ''
  type: Blog
  url: https://www.concur.com/newsroom
- title: ''
  type: SignUp
  url: https://developer.concur.com/register
- title: ''
  type: GitHubRepository
  url: https://github.com/SAP-docs/preview.developer.concur.com
- title: ''
  type: ReleaseNotes
  url: https://developer.concur.com/tools-support/release-notes/
- title: ''
  type: ChangeLog
  url: https://developer.concur.com/tools-support/release-notes/
- title: SAP Business Accelerator Hub
  type: Resources
  url: https://api.sap.com/products/SAPConcur/apis/REST
- title: ''
  type: Tutorials
  url: https://developers.sap.com/tutorials/data-to-value-conn-concur-part01..html
created: '2024'
description: SAP Concur is a leading provider of integrated travel, expense, and invoice management solutions. Their APIs enable developers to integrate Concur functionality into their applications, automate business processes, and access travel and expense data.
features:
- description: Secure token-based authentication supporting both company-level and user-level access tokens with automatic refresh.
  name: OAuth 2.0 Authentication
- description: Separate API endpoints for US, US2, EMEA, and China datacenters ensuring data residency compliance.
  name: Multi-Datacenter Support
- description: Publish/Subscribe event-driven architecture for real-time notifications on business events like report submissions.
  name: Event Subscription Service
- description: Standards-based user identity management following SCIM protocol for automated user lifecycle operations.
  name: SCIM 2.0 User Provisioning
- description: Integration framework allowing travel suppliers to provide inventory directly to the Concur booking tool.
  name: Direct Connect Framework
- description: Custom exchange rate management supporting bulk uploads for currency conversion across global operations.
  name: Multi-Currency Exchange Rates
image: https://www.concur.com/themes/custom/concur/logo.svg
integrations:
- description: Native integration with SAP S/4HANA and SAP ERP for financial posting, cost center sync, and master data management.
  name: SAP ERP
- description: Approve expense reports and travel requests directly from Microsoft Teams notifications.
  name: Microsoft Teams
- description: Automatic e-receipt submission for Uber business rides directly into Concur Expense.
  name: Uber for Business
- description: Sync customer and opportunity data to pre-populate expense reports and travel requests.
  name: Salesforce
- description: Automated financial posting of approved expense reports and invoices into Oracle NetSuite.
  name: Oracle NetSuite
jsonld:
- class_count: 0
  name: Sap Concur Context
  property_count: 15
  slug: sap-concur-context
- class_count: 0
  name: Sap Concur Expense Context
  property_count: 0
  slug: sap-concur-expense-context
layout: provider
modified: '2026-04-18'
name: SAP Concur
rules:
- name: SAP Concur API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: sap-concur-spectral-rules
skills: []
slug: sap-concur
solutions: []
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
url: https://www.concur.com
use_cases:
- description: Automate expense report creation, submission, and approval workflows by integrating with ERP and financial systems.
  name: Expense Report Automation
- description: Connect travel management companies and suppliers to provide booking, itinerary, and receipt data within Concur Travel.
  name: Travel Booking Integration
- description: Streamline accounts payable by automating invoice creation, purchase order matching, and vendor management.
  name: Invoice Processing
- description: Extract approved expense reports and invoices for automated posting into ERP systems like SAP, Oracle, and NetSuite.
  name: Financial Posting
- description: Submit and manage digital receipts from e-receipt partners and mobile capture for paperless expense management.
  name: Receipt Digitization
---
