---
api_count: 7
apis:
- description: SOAP and OData web services for interacting with Dynamics NAV business data. Supports publishing pages, codeunits, and queries as web services for external system integration.
  name: Dynamics NAV Web Services API
  slug: ''
- description: OData web services for querying and manipulating NAV business entities. Supports both OData v3 and v4 protocols for reading data and writing back to the Dynamics NAV database through exposed pages and
  name: Dynamics NAV OData API
  slug: ''
- description: SOAP-based web services for legacy integrations and business logic operations in Dynamics NAV. Exposes pages and codeunits with built-in CRUD operations and supports extension codeunits for custom ope
  name: Dynamics NAV SOAP Web Services
  slug: ''
- description: Modern RESTful API for Dynamics 365 Business Central, the cloud evolution of Dynamics NAV. Provides a comprehensive set of endpoints for managing customers, items, accounts, sales orders, and other bu
  name: Business Central API v2.0
  slug: ''
- description: REST API for programmatic administration of Business Central environments. Enables querying and managing production and sandbox environments, setting up notifications, and viewing tenant telemetry.
  name: Business Central Administration Center API
  slug: ''
- description: API for automating company setup and tenant management in Business Central. Supports creating companies, installing extensions, assigning permissions, and applying RapidStart packages programmatically
  name: Business Central Automation API
  slug: ''
- description: RESTful web services layer for Business Central that provides the preferred integration method. Includes built-in APIs, custom API pages and queries, and supports both on-premises and cloud deployment
  name: Business Central REST API Web Services
  slug: ''
capabilities:
- description: Unified workflow for day-to-day business operations in Dynamics 365 Business Central combining the Business Central API v2.0 for managing customers, vendors, items, orders, invoices, and financials. U
  name: Dynamics NAV Business Operations
  slug: business-operations
- description: Unified workflow for administering Dynamics 365 Business Central combining the Administration Center API for environment management with the Automation API for company setup, extensions, users, and pe
  name: Dynamics NAV Platform Administration
  slug: platform-administration
common:
- title: ''
  type: Portal
  url: https://dynamics.microsoft.com
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-get-started
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/users-credential-types
- title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/product/dynamics-365-business-central/
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/overview
- title: ''
  type: Support
  url: https://support.microsoft.com/dynamics
- title: ''
  type: SignUp
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/trial-signup
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/dynamics-365/products/business-central/pricing
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en/dynamics-365/business-applications/legal
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com
- title: ''
  type: StatusPage
  url: https://status.cloud.microsoft
- title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/BCApps
- title: ''
  type: GitHubRepository
  url: https://github.com/christianbraeunlich/d365bc-api-postman
- title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/dynamics-rate-limits
- title: Laravel SDK
  type: SDK
  url: https://github.com/niclas-timm/laravel-dynamics-365-business-central
- title: Go REST Client
  type: SDK
  url: https://github.com/AgoraIO/agora-rest-client-go
- title: AL Language CLI
  type: CLI
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-command-line-tools
- title: Customer Schema
  type: JSONSchema
  url: json-schema/customer.json
- title: Vendor Schema
  type: JSONSchema
  url: json-schema/vendor.json
- title: Item Schema
  type: JSONSchema
  url: json-schema/item.json
- title: Sales Order Schema
  type: JSONSchema
  url: json-schema/sales-order.json
- title: Purchase Order Schema
  type: JSONSchema
  url: json-schema/purchase-order.json
- title: BC v2 Customer Schema
  type: JSONSchema
  url: json-schema/business-central-v2-customer-schema.json
- title: BC v2 Vendor Schema
  type: JSONSchema
  url: json-schema/business-central-v2-vendor-schema.json
- title: BC v2 Item Schema
  type: JSONSchema
  url: json-schema/business-central-v2-item-schema.json
- title: BC v2 Sales Order Schema
  type: JSONSchema
  url: json-schema/business-central-v2-sales-order-schema.json
- title: BC v2 Purchase Order Schema
  type: JSONSchema
  url: json-schema/business-central-v2-purchase-order-schema.json
- title: Admin Center Environment Schema
  type: JSONSchema
  url: json-schema/admin-center-environment-schema.json
- title: Admin Center Environment Operation Schema
  type: JSONSchema
  url: json-schema/admin-center-environment-operation-schema.json
- title: Automation Extension Schema
  type: JSONSchema
  url: json-schema/automation-extension-schema.json
- title: Automation User Schema
  type: JSONSchema
  url: json-schema/automation-user-schema.json
- title: Automation Company Schema
  type: JSONSchema
  url: json-schema/automation-automation-company-schema.json
- title: JSON-LD Context
  type: JSONLD
  url: json-ld/context.jsonld
- title: Business Central v2 JSON-LD Context
  type: JSONLD
  url: json-ld/business-central-v2-context.jsonld
- title: Admin Center JSON-LD Context
  type: JSONLD
  url: json-ld/admin-center-context.jsonld
- title: Automation JSON-LD Context
  type: JSONLD
  url: json-ld/automation-context.jsonld
- title: Navision Vocabulary
  type: Vocabulary
  url: vocabulary/navision-vocabulary.yaml
- title: Spectral Rules
  type: Rules
  url: rules/navision-spectral-rules.yml
- title: Business Operations Workflow
  type: Capabilities
  url: capabilities/business-operations.yaml
- title: Platform Administration Workflow
  type: Capabilities
  url: capabilities/platform-administration.yaml
- title: Business Central v2 Shared Capability
  type: Capabilities
  url: capabilities/shared/business-central-v2.yaml
- title: Admin Center Shared Capability
  type: Capabilities
  url: capabilities/shared/admin-center.yaml
- title: Automation Shared Capability
  type: Capabilities
  url: capabilities/shared/automation.yaml
created: '2024-01-20'
description: API collection for Microsoft Dynamics NAV (formerly Navision), an enterprise resource planning (ERP) solution for small and medium-sized businesses. Dynamics NAV has evolved into Dynamics 365 Business Central, which provides modern REST, OData, and SOAP web services for business data integration.
features:
- description: General ledger, accounts payable/receivable, bank reconciliation, and financial reporting
  name: Financial Management
- description: Create and manage sales orders, invoices, credit memos, and quotes
  name: Sales Order Management
- description: Manage purchase orders, invoices, and vendor relationships
  name: Purchase Order Management
- description: Track items, stock levels, and inventory valuations
  name: Inventory Management
- description: Programmatic management of production and sandbox environments
  name: Environment Administration
- description: Automate company setup, extension management, and user provisioning
  name: Tenant Automation
image: /assets/icons/navision.png
integrations:
- description: Deep integration with Excel, Outlook, and Teams for business workflows
  name: Microsoft 365
- description: Connect to Power BI, Power Automate, and Power Apps
  name: Power Platform
- description: Sync orders, customers, and inventory with Shopify stores
  name: Shopify
jsonld:
- class_count: 0
  name: Admin Center Context
  property_count: 0
  slug: admin-center-context
- class_count: 0
  name: Automation Context
  property_count: 0
  slug: automation-context
- class_count: 0
  name: Business Central V2 Context
  property_count: 0
  slug: business-central-v2-context
- class_count: 0
  name: context Context
  property_count: 9
  slug: context
layout: provider
modified: '2026-04-18'
name: Microsoft Dynamics NAV
rules:
- name: Microsoft Dynamics NAV API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: navision-spectral-rules
skills: []
slug: navision
solutions: []
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
url: https://dynamics.microsoft.com/nav-overview/
use_cases:
- description: Connect external systems to Business Central for real-time business data sync
  name: ERP Integration
- description: Automate company creation and configuration across Business Central tenants
  name: Multi-Company Management
- description: Extract general ledger entries and account data for custom reporting
  name: Financial Reporting
---
