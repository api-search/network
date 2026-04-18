---
api_count: 19
apis:
- description: RESTful API for accessing SAP Business One data and business logic.
  name: SAP Business One Service Layer API
  slug: ''
- description: APIs for SAP S/4HANA Cloud enabling integration with intelligent ERP.
  name: SAP S/4HANA Cloud API
  slug: ''
- description: Human Capital Management APIs for employee central, recruiting, and talent management.
  name: SAP SuccessFactors API
  slug: ''
- description: Procurement and supply chain APIs for sourcing, contracts, and supplier management.
  name: SAP Ariba APIs
  slug: ''
- description: Integration APIs for connecting applications, data, and processes.
  name: SAP Cloud Platform Integration Suite
  slug: ''
- description: E-commerce APIs for product catalog, cart, checkout, and order management.
  name: SAP Commerce Cloud API
  slug: ''
- description: APIs for business intelligence, planning, and predictive analytics.
  name: SAP Analytics Cloud API
  slug: ''
- description: APIs for travel and expense management including expense reporting, travel booking, and invoice processing.
  name: SAP Concur API
  slug: ''
- description: Vendor management system APIs for managing external workers, contractors, and service providers.
  name: SAP Fieldglass API
  slug: ''
- description: Core platform APIs for managing accounts, entitlements, and services on SAP Business Technology Platform.
  name: SAP BTP Core Services API
  slug: ''
- description: APIs for data warehousing, catalog access, and consumption of analytical and relational models.
  name: SAP Datasphere API
  slug: ''
- description: Messaging APIs for event-driven architecture supporting AMQP, MQTT, and REST protocols.
  name: SAP Event Mesh API
  slug: ''
- description: APIs for centralizing and harmonizing master data across SAP and third-party applications.
  name: SAP Master Data Integration API
  slug: ''
- description: APIs for process modeling, BPMN diagram management, and process governance automation.
  name: SAP Signavio Process Manager API
  slug: ''
- description: CMIS-based APIs for document management including versioning, access control, and content storage on BTP.
  name: SAP Document Management Service API
  slug: ''
- description: APIs for building, managing, publishing, and monitoring API proxies within SAP Integration Suite.
  name: SAP Integration Suite API Management
  slug: ''
- description: APIs for deploying, managing, and consuming AI models and workflows on SAP Business Technology Platform. Provides endpoints for scenario management, execution orchestration, and model serving.
  name: SAP AI Core API
  slug: ''
- description: REST APIs for marketing automation, customer engagement, and personalized campaign management across email, web, SMS, and mobile channels.
  name: SAP Emarsys Customer Engagement API
  slug: ''
- description: APIs for managing digital workplace experiences, integrating business applications into unified workpages, and administering work zone sites and content.
  name: SAP Build Work Zone API
  slug: ''
asyncapis:
- description: Event-driven messaging API for SAP Business Technology Platform supporting AMQP, MQTT, and REST protocols. Enables publish/subscribe patterns for business events across SAP and third-party application
  name: SAP Event Mesh Events
  slug: sap-event-mesh-asyncapi
capabilities:
- description: Unified workflow combining SAP Business One, S/4HANA Cloud Business Partner, and AI Core APIs for managing business partners, orders, financials, and AI-driven automation across SAP ERP systems.
  name: SAP Enterprise Business Operations
  slug: enterprise-business-operations
common:
- title: ''
  type: DeveloperPortal
  url: https://developers.sap.com/
- title: ''
  type: Hub
  url: https://api.sap.com
- title: ''
  type: Blog
  url: https://community.sap.com/t5/all-sap-community-blogs/ct-p/all-blogs
- title: ''
  type: Support
  url: https://community.sap.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/SAP
- title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- title: ''
  type: Support
  url: https://support.sap.com/
- title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- title: ''
  type: GettingStarted
  url: https://developers.sap.com/tutorial-navigator.html
- title: ''
  type: Training
  url: https://learning.sap.com/
- title: ''
  type: Portal
  url: https://www.sap.com
- title: ''
  type: SignUp
  url: https://developers.sap.com/tutorials/hcp-create-trial-account.html
- title: ''
  type: Login
  url: https://accounts.sap.com
- title: ''
  type: SDK
  url: https://developers.sap.com/topics/cloud-sdk.html
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/sap
- title: ''
  type: YouTube
  url: https://www.youtube.com/@SAPTechnology
- title: ''
  type: ChangeLog
  url: https://help.sap.com/whats-new/
- title: ''
  type: JSONLD
  url: json-ld/sap-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/sap-business-partner-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/sap-sales-order-schema.json
- title: ''
  type: Rules
  url: rules/sap-spectral-rules.yml
- title: ''
  type: Capabilities
  url: capabilities/shared/ai-core.yaml
- title: ''
  type: Capabilities
  url: capabilities/shared/business-one.yaml
- title: ''
  type: Capabilities
  url: capabilities/shared/s4hana-business-partner.yaml
- title: ''
  type: Capabilities
  url: capabilities/enterprise-business-operations.yaml
created: '2024-01-15'
description: Collection of SAP's enterprise APIs for business applications and cloud services.
features:
- ERP and business suite APIs for finance, HR, procurement, and supply chain
- AI/ML model deployment and serving via AI Core on BTP
- Master data management and integration across SAP and third-party systems
- Event-driven architecture with AMQP, MQTT, and REST messaging
- OData-compatible endpoints for business object CRUD operations
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
integrations:
- SAP S/4HANA Cloud with CRM and e-commerce platforms
- SAP AI Core with machine learning frameworks and model registries
- SAP Integration Suite with middleware and iPaaS connectors
- SAP SuccessFactors with HR and talent management systems
- SAP Event Mesh with event-driven microservices architectures
jsonld:
- class_count: 0
  name: Sap Ai Core Context
  property_count: 0
  slug: sap-ai-core-context
- class_count: 0
  name: Sap Business One Service Layer Context
  property_count: 0
  slug: sap-business-one-service-layer-context
- class_count: 0
  name: Sap Context
  property_count: 8
  slug: sap-context
- class_count: 0
  name: Sap S4Hana Cloud Business Partner Context
  property_count: 0
  slug: sap-s4hana-cloud-business-partner-context
layout: provider
modified: '2026-04-18'
name: SAP
rules:
- name: SAP API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: sap-spectral-rules
skills: []
slug: sap
solutions: []
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
url: https://api.sap.com
use_cases:
- Automating order-to-cash and procure-to-pay business processes
- Deploying and serving AI models for intelligent enterprise workflows
- Integrating SAP ERP with third-party CRM, e-commerce, and analytics platforms
- Managing business partner master data across multi-system landscapes
- Building digital workplace experiences with unified work zone portals
---
