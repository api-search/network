---
api_count: 18
apis:
- description: API for creating, reading, updating, and deleting business partner master data.
  name: SAP S/4HANA Business Partner API
  slug: ''
- description: API for managing sales orders including creation, updates, and status changes.
  name: SAP S/4HANA Sales Order API
  slug: ''
- description: API for creating and managing purchase orders in procurement processes.
  name: SAP S/4HANA Purchase Order API
  slug: ''
- description: API for posting goods movements and managing inventory transactions.
  name: SAP S/4HANA Material Document API
  slug: ''
- description: API for managing product and material master data.
  name: SAP S/4HANA Product Master API
  slug: ''
- description: API for creating and managing financial journal entries.
  name: SAP S/4HANA Journal Entry API
  slug: ''
- description: API for reading, canceling, and retrieving PDFs of billing documents in sales and distribution.
  name: SAP S/4HANA Billing Document API
  slug: ''
- description: API for creating and processing supplier invoices referenced to purchase orders.
  name: SAP S/4HANA Supplier Invoice API
  slug: ''
- description: API for integrating external applications with customer return processing including advanced returns management.
  name: SAP S/4HANA Customer Return API
  slug: ''
- description: API for creating, updating, and managing purchase requisitions in procurement workflows.
  name: SAP S/4HANA Purchase Requisition API
  slug: ''
- description: API for creating, reading, updating, and deleting outbound deliveries including goods issue and picking operations.
  name: SAP S/4HANA Outbound Delivery API
  slug: ''
- description: API for creating, reading, updating, and deleting inbound deliveries for procurement and logistics.
  name: SAP S/4HANA Inbound Delivery API
  slug: ''
- description: API for reading cost center master data used in controlling and cost management.
  name: SAP S/4HANA Cost Center API
  slug: ''
- description: API for reading general ledger account master data in chart of accounts.
  name: SAP S/4HANA GL Account API
  slug: ''
- description: API for reading bank master data including bank keys, SWIFT codes, and bank details.
  name: SAP S/4HANA Bank Master API
  slug: ''
- description: API for reading production order data including components, operations, and status information.
  name: SAP S/4HANA Production Order API
  slug: ''
- description: API for reading maintenance order data used in plant maintenance and enterprise asset management.
  name: SAP S/4HANA Maintenance Order API
  slug: ''
- description: API for creating, reading, updating, and deleting workforce timesheet entries with automatic posting to controlling.
  name: SAP S/4HANA Workforce Timesheet API
  slug: ''
capabilities:
- description: Unified order-to-cash capability combining sales order management with items, partners, pricing, schedule lines, and text records. Used by sales operations and order management teams.
  name: SAP S/4HANA Order-to-Cash
  slug: order-to-cash
common:
- title: ''
  type: Portal
  url: https://api.sap.com
- title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/1e45cfd73e814aa6b1a1118e2c1d3cec.html
- title: ''
  type: Authentication
  url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/26f2b5aa3f3a4019b7d08978095b9e6a.html
- title: ''
  type: ChangeLog
  url: https://api.sap.com/releasenotes
- title: ''
  type: Support
  url: https://support.sap.com
- title: ''
  type: TermsOfService
  url: https://www.sap.com/about/trust-center/agreements/cloud/cloud-services.html
- title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- title: ''
  type: API Catalog
  url: https://api.sap.com/products/SAPS4HANACloud/apis/all
- title: ''
  type: API Packages
  url: https://api.sap.com/products/SAPS4HANACloud/apis/packages
- title: ''
  type: OData V4 APIs
  url: https://api.sap.com/products/SAPS4HANACloud/apis/ODATAV4
- title: ''
  type: REST APIs
  url: https://api.sap.com/products/SAPS4HANACloud/apis/REST
- title: ''
  type: On-Premise API Catalog
  url: https://api.sap.com/products/SAPS4HANA/apis/all
- title: ''
  type: On-Premise API Packages
  url: https://api.sap.com/products/SAPS4HANA/apis/packages
- title: ''
  type: Private Edition APIs
  url: https://api.sap.com/products/SAPS4HANACloudPrivateEdition/apis/packages
- title: ''
  type: Community
  url: https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-apis-and-where-to-find-them/ba-p/13723939
- title: ''
  type: StatusPage
  url: https://www.sap.com/about/cloud-trust-center/cloud-service-status.html
created: '2024-01-15'
description: Collection of SAP S/4HANA Cloud and On-Premise APIs for enterprise resource planning.
features:
- description: RESTful APIs following OData protocol for standardized CRUD operations and query capabilities.
  name: OData V2 and V4 APIs
- description: Create complex documents with header and dependent entities in a single API request.
  name: Deep Insert
- description: ETag-based concurrency control to prevent conflicting updates to business documents.
  name: Optimistic Concurrency
- description: Synchronous API access to live ERP data for real-time business process integration.
  name: Real-Time Integration
- description: APIs spanning finance, sales, procurement, logistics, manufacturing, and HR modules.
  name: Multi-Module Coverage
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
integrations:
- description: Native integration with SAP BTP for extensions, analytics, and AI/ML capabilities.
  name: SAP Business Technology Platform
- description: Pre-built integration flows for connecting S/4HANA with third-party applications.
  name: SAP Integration Suite
- description: Integration with Excel and Outlook for business data analysis and communication workflows.
  name: Microsoft Office
jsonld:
- class_count: 10
  name: Sap S4Hana Context
  property_count: 14
  slug: sap-s4hana-context
- class_count: 0
  name: Sap S4Hana Sales Order Context
  property_count: 0
  slug: sap-s4hana-sales-order-context
layout: provider
modified: '2026-04-18'
name: SAP S/4HANA
rules:
- name: SAP S/4HANA API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: sap-s4hana-spectral-rules
skills: []
slug: sap-s4hana
solutions: []
tags:
- Business Applications
- Cloud
- Enterprise Resource Planning
- ERP
- Finance
- Human Resources
- Inventory
- Logistics
- Manufacturing
- Plant Maintenance
- Procurement
- S/4HANA
- Sales
- SAP
url: https://api.sap.com/apis.json
use_cases:
- description: Automate the sales process from sales order creation through delivery and billing.
  name: Order-to-Cash
- description: Streamline procurement from purchase requisition through purchase order, receipt, and invoice.
  name: Procure-to-Pay
- description: Automate journal entries, cost center reporting, and GL account management for period close.
  name: Financial Close
- description: Track inbound and outbound deliveries, inventory movements, and material documents in real time.
  name: Supply Chain Visibility
---
