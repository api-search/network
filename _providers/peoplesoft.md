---
api_count: 31
apis:
- description: RESTful web services for PeopleSoft applications enabling integration with external systems via the PeopleTools platform.
  name: PeopleSoft REST API
  slug: rest-api
- description: Modern REST API layer introduced in PeopleTools 8.59 that produces fully compliant OpenAPI/Swagger specifications, supports proper HTTP status codes, uniform URLs, and JSON payloads for integration wi
  name: PeopleSoft Application Services Framework API
  slug: application-services-framework-api
- description: Message-based integration framework for synchronous and asynchronous communication supporting both SOAP and REST protocols.
  name: PeopleSoft Integration Broker
  slug: integration-broker
- description: Execute PeopleSoft Query definitions and retrieve results via REST including the Query Access Service operations for listing, executing, and managing queries.
  name: PeopleSoft Query API
  slug: query-api
- description: Programmatic access to PeopleSoft components for data manipulation providing CRUD operations on component data via REST.
  name: PeopleSoft Component Interface API
  slug: component-interface-api
- description: Search indexing and query capabilities powered by OpenSearch (previously Elasticsearch) for full-text search, analytics dashboards, and PeopleSoft Insights.
  name: PeopleSoft Search Framework API
  slug: search-framework-api
- description: Framework for extracting and flattening PeopleSoft data for machine learning and analytics purposes. Uses PeopleSoft Search Framework technology with OpenSearch to build, index, and register data mode
  name: PeopleSoft Data Distribution Framework API
  slug: data-distribution-framework-api
- description: Push notification and event-driven notification services including the Notification Composer for email, text, and in-app notifications. Requires PeopleTools 8.59.19+.
  name: PeopleSoft Notification Framework API
  slug: notification-framework-api
- description: Integration framework for connecting PeopleSoft with Oracle Digital Assistant (ODA) including REST services for chatbot data retrieval and embedded chatbot UI on Fluid pages (PICASO). Requires PeopleT
  name: PeopleSoft Chatbot Integration Framework API
  slug: chatbot-integration-framework-api
- description: Framework for creating, running, and managing approval processes exposable via REST service operations through Integration Broker or ASF.
  name: PeopleSoft Approval Workflow Engine API
  slug: approval-workflow-engine-api
- description: Process request APIs for submitting and scheduling batch jobs, monitoring process run status, viewing logs, and Application Engine batch processing statistics.
  name: PeopleSoft Process Scheduler API
  slug: process-scheduler-api
- description: REST APIs for automated environment provisioning and deployment on Oracle Cloud Infrastructure including PeopleTools upgrades, update management, and self-service provisioning templates.
  name: PeopleSoft Cloud Manager API
  slug: cloud-manager-api
- description: REST services for automated update image management, change package generation, and PeopleSoft Automated Updates (PAU).
  name: PeopleSoft Update Manager API
  slug: update-manager-api
- description: Operational dashboard reporting using PS Query, Composite Query, or component data sources accessible via web services for analytics and visualization.
  name: PeopleSoft Pivot Grid API
  slug: pivot-grid-api
- description: Human Capital Management APIs for employee data, benefits, payroll, workforce administration, and talent management.
  name: PeopleSoft HCM API
  slug: hcm-api
- description: REST API for retrieving employee details by name or employee ID, and for looking up direct reports based on manager name or ID. Supports the Employee Directory chatbot skill and integration with exter
  name: PeopleSoft Employee Directory API
  slug: employee-directory-api
- description: REST API for creating, updating, and retrieving absence requests, viewing employee absence balances by type, and retrieving absence configuration rules. Supports Absence Management chatbot skill and s
  name: PeopleSoft Absence Management API
  slug: absence-management-api
- description: REST endpoints for job search services, Candidate Gateway self-service, recruiting solutions, and talent management workflows.
  name: PeopleSoft Recruiting and Talent Management API
  slug: recruiting-and-talent-management-api
- description: Delivered REST API endpoints for retrieving paycheck header details, earnings, deductions, taxes, direct deposits, employer paid benefits, garnishments, and year-end forms for North American payroll p
  name: PeopleSoft Payroll for North America API
  slug: payroll-for-north-america-api
- description: REST API endpoints for the Global Payroll skill, providing access to payroll data, product profile information, and chatbot framework resources for international payroll processing across multiple cou
  name: PeopleSoft Global Payroll API
  slug: global-payroll-api
- description: REST API for retrieving employee country and business partner contact details. Shared utility services used across all delivered HCM skills and integration scenarios.
  name: PeopleSoft HR Common Utility Services API
  slug: hr-common-utility-services-api
- description: Financial Management APIs for general ledger, accounts payable, accounts receivable, expenses, asset management, and financial reporting.
  name: PeopleSoft Financials API
  slug: financials-api
- description: 'Delivered REST API endpoints for expense report management including fetching expense reports by status, creation date, or sheet name, retrieving transaction details, managing wallet entries, expense '
  name: PeopleSoft Expenses API
  slug: expenses-api
- description: Delivered REST API endpoints for invoice and payment management including fetching disputed invoices, invoice status inquiries, payment status tracking, payment inquiries, and payment difference resol
  name: PeopleSoft eSettlements API
  slug: esettlements-api
- description: REST API endpoints for procurement, inventory management, order fulfillment, logistics, and enterprise integration points for warehouse management systems.
  name: PeopleSoft Supply Chain Management API
  slug: supply-chain-management-api
- description: Delivered REST API endpoints for requisition management including retrieving requisitions for items, getting requester lists and names, and checking requisition status. Supports the full procure-to-pa
  name: PeopleSoft eProcurement API
  slug: eprocurement-api
- description: Comprehensive REST API for the Supplier Portal providing access to bid details, managed content such as announcements and events, overdue shipment tracking, purchase order acknowledgement, invoice and
  name: PeopleSoft Supplier Portal API
  slug: supplier-portal-api
- description: Customer Relationship Management REST API endpoints and integration points for customer data, case management, sales, and marketing.
  name: PeopleSoft CRM API
  slug: crm-api
- description: Campus Solutions APIs for student records, admissions, enrollment, financial aid, and academic advising.
  name: PeopleSoft Campus Solutions API
  slug: campus-solutions-api
- description: Analytics, budgeting, forecasting, and planning APIs with events and notifications framework for financial and operational performance management.
  name: PeopleSoft Enterprise Performance Management API
  slug: enterprise-performance-management-api
- description: Content management, branding, and portal administration APIs for the PeopleSoft Interaction Hub (formerly Enterprise Portal) with Integration Broker services.
  name: PeopleSoft Interaction Hub API
  slug: interaction-hub-api
capabilities:
- description: Unified workflow for campus administrators combining student records, admissions, enrollment, financial aid, and approval workflows across PeopleSoft Campus Solutions and Approval Workflow Engine APIs
  name: PeopleSoft Campus Administration
  slug: campus-administration
- description: Unified workflow for CRM users combining customer management, case management, sales, chatbot integration, and notifications across PeopleSoft CRM, Chatbot Integration, and Notification Framework APIs
  name: PeopleSoft Customer Engagement
  slug: customer-engagement
- description: Unified workflow for finance controllers combining general ledger, accounts payable, accounts receivable, expenses, budgeting, forecasting, analytics, and approval workflows across PeopleSoft Financia
  name: PeopleSoft Finance And Accounting
  slug: finance-and-accounting
- description: 'Unified workflow for HR administrators combining employee management, benefits, payroll, recruiting, talent management, and approval workflows across PeopleSoft HCM, Recruiting, and Approval Workflow '
  name: PeopleSoft Human Resources
  slug: human-resources
- description: Unified workflow for IT administrators combining environment provisioning, update management, process scheduling, integration broker, REST API management, application services framework, and component
  name: PeopleSoft Platform Administration
  slug: platform-administration
- description: Unified workflow for content managers combining portal content management, branding, chatbot integration, and notification services across PeopleSoft Interaction Hub, Chatbot Integration, and Notifica
  name: PeopleSoft Portal And Communications
  slug: portal-and-communications
- description: Unified workflow for analysts combining query execution, pivot grid dashboards, full-text search, and performance analytics across PeopleSoft Query, Pivot Grid, Search Framework, and EPM APIs.
  name: PeopleSoft Reporting And Analytics
  slug: reporting-and-analytics
- description: Unified workflow for supply chain managers combining procurement, inventory, order fulfillment, and approval workflows across PeopleSoft Supply Chain Management and Approval Workflow Engine APIs.
  name: PeopleSoft Supply Chain And Procurement
  slug: supply-chain-and-procurement
common:
- title: ''
  type: Portal
  url: https://www.oracle.com/applications/peoplesoft/
- title: ''
  type: Documentation
  url: https://docs.oracle.com/en/applications/peoplesoft/index.html
- title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/applications/peoplesoft/peopletools/index.html
- title: ''
  type: Information Portal
  url: https://docs.oracle.com/cd/E52319_01/infoportal/
- title: ''
  type: Authentication
  url: https://docs.oracle.com/cd/F30998_01/pt858pbr2/eng/pt/tsec/concept_UnderstandingOAuth2_0.html
- title: ''
  type: Blog
  url: https://blogs.oracle.com/peoplesoft/
- title: ''
  type: ChangeLog
  url: https://blogs.oracle.com/peoplesoft/category/ps-image-and-release-updates
- title: ''
  type: PeopleCode API Reference
  url: https://docs.oracle.com/cd/E25688_01/pt852pbr0/eng/psbooks/tpcr/book.htm
- title: ''
  type: Security
  url: https://www.oracle.com/security-alerts/
- title: ''
  type: Support
  url: https://support.oracle.com/
- title: ''
  type: Knowledge Base
  url: https://docs.oracle.com/en/applications/peoplesoft/
- title: ''
  type: Community
  url: https://community.oracle.com/customerconnect/categories/peoplesoft
- title: ''
  type: Forum
  url: https://forums.oracle.com/ords/apexds/domain/dev-community/category/peoplesoft_enterprise
- title: ''
  type: PeopleSoft on OCI
  url: https://docs.oracle.com/cd/E52319_01/infoportal/opc.html
- title: ''
  type: Training
  url: https://education.oracle.com/peoplesoft
- title: ''
  type: Videos
  url: https://docs.oracle.com/cd/E52319_01/infoportal/videos.html
- title: ''
  type: Pricing
  url: https://www.oracle.com/corporate/pricing/
- title: ''
  type: TermsOfService
  url: https://www.oracle.com/contracts/
- title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/services-privacy-policy/
- title: ''
  type: News
  url: https://docs.oracle.com/cd/E52319_01/infoportal/news.html
- title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- title: ''
  type: Website
  url: https://www.oracle.com/applications/peoplesoft/
- title: ''
  type: Login
  url: https://cloud.oracle.com/
- title: ''
  type: SignUp
  url: https://cloud.oracle.com/
- title: ''
  type: REST API Endpoints
  url: https://docs.oracle.com/cd/G36917_01/ps91pbr20/eng/ps/eccp/UnderstandingRestApiEndpointsForPeoplesoft.html
created: '2024-01-15'
description: Collection of Oracle PeopleSoft Enterprise application APIs for Human Capital Management, Financial Management, Supply Chain Management, CRM, Campus Solutions, and engineering intelligence across PeopleTools platform services.
features:
- description: RESTful APIs via PeopleTools Integration Broker for JSON-based integration with external systems.
  name: REST Web Services
- description: Modern REST API layer with OpenAPI spec generation, proper HTTP status codes, and JSON payloads.
  name: Application Services Framework
- description: Enterprise messaging and integration platform supporting SOAP, REST, and asynchronous messaging.
  name: Integration Broker
- description: Programmatic access to PeopleSoft component business logic for data entry and validation.
  name: Component Interface API
- description: Execute PeopleSoft queries and retrieve results via REST for reporting and analytics.
  name: Query API
- description: Human Capital Management APIs for workforce administration, benefits, payroll, and talent management.
  name: HCM APIs
- description: APIs for general ledger, accounts payable/receivable, asset management, and procurement.
  name: Financial Management APIs
- description: APIs for inventory, purchasing, order management, and supplier collaboration.
  name: Supply Chain Management APIs
- description: APIs for student records, admissions, financial aid, and academic advisement.
  name: Campus Solutions APIs
- description: Standards-based OAuth 2.0 authentication for secure API access.
  name: OAuth 2.0 Authentication
- description: APIs for integrating with PeopleSoft Fluid user interface framework.
  name: Fluid UI Integration
- description: Digital assistant and chatbot framework APIs for conversational PeopleSoft interactions.
  name: Chatbot Integration
image: https://www.oracle.com/a/ocom/img/cb71-psft-logo.jpg
integrations: []
jsonld:
- class_count: 8
  name: Peoplesoft Context
  property_count: 77
  slug: peoplesoft-context
layout: provider
modified: '2026-04-17'
name: PeopleSoft
rules:
- name: PeopleSoft API Rules
  rule_count: 19
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 4
  slug: peoplesoft-spectral-rules
skills: []
slug: peoplesoft
solutions:
- description: Human Capital Management for workforce administration, benefits, payroll, talent, and workforce planning.
  name: PeopleSoft HCM
- description: Financial and Supply Chain Management for general ledger, AP/AR, procurement, and inventory.
  name: PeopleSoft FSCM
- description: Higher education platform for student records, admissions, financial aid, and academic management.
  name: PeopleSoft Campus Solutions
- description: Customer Relationship Management for sales, marketing, and service automation.
  name: PeopleSoft CRM
tags:
- Campus Solutions
- CRM
- Enterprise Software
- ERP
- Financial Management
- HCM
- Supply Chain Management
url: https://raw.githubusercontent.com/api-evangelist/peoplesoft/refs/heads/main/apis.yml
use_cases:
- description: Integrate HCM data with payroll, benefits, and talent management platforms.
  name: HR System Integration
- description: Exchange financial transactions and reporting data with external ERP and accounting systems.
  name: Financial Data Exchange
- description: Integrate campus solutions with learning management and student portal systems.
  name: Student Information System
- description: Automate procurement, inventory, and supplier management workflows.
  name: Supply Chain Automation
- description: Build employee and student self-service applications using PeopleSoft APIs.
  name: Self-Service Portals
- description: Power mobile apps for employee self-service, approvals, and time entry.
  name: Mobile Applications
- description: Connect PeopleSoft with Oracle Integration Cloud and other cloud platforms.
  name: Cloud Integration
- description: Extract data via Query API for business intelligence and analytics platforms.
  name: Reporting and Analytics
---
