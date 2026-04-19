---
api_count: 4
apis:
- description: Developer API for Oracle Integration 3 providing day-to-day management of integrations, connections, packages, libraries, lookups, certificates, scheduled integrations, monitoring, B2B trading partner
  name: Oracle Integration Developer API
  slug: ''
- description: REST API for Oracle Cloud Infrastructure Process Automation enabling management of process definitions, process instances, tasks, decision models, dynamic processes, identities, spaces, analytics, and
  name: Oracle Integration Process Automation API
  slug: ''
- description: REST API for configuring and administering the Oracle Integration File Server, an SFTP-compliant file repository for managing file-based integrations.
  name: Oracle Integration File Server API
  slug: ''
- description: OCI control plane API for provisioning and managing Oracle Integration instances, custom endpoints, and data retention configuration.
  name: Oracle Integration Administrative API
  slug: ''
capabilities:
- description: Unified workflow for managing Oracle Integration lifecycle including integrations, connections, packages, monitoring, B2B trading partners, process automation, tasks, and decision models. Used by inte
  name: Oracle Integration Management
  slug: integration-management
common:
- title: ''
  type: Portal
  url: https://cloud.oracle.com/integration
- title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/paas/application-integration/oracle-integration-oci/explore-oracle-integration-apis.html
- title: ''
  type: Tutorials
  url: https://docs.oracle.com/en/cloud/paas/integration-cloud/tutorials.html
- title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/paas/application-integration/index.html
- title: ''
  type: Blog
  url: https://blogs.oracle.com/integration/
- title: ''
  type: ChangeLog
  url: https://docs.oracle.com/en/cloud/paas/integration-cloud/whats-new/
- title: ''
  type: Support
  url: https://www.oracle.com/support/
- title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- title: ''
  type: Pricing
  url: https://www.oracle.com/integration/pricing/
- title: ''
  type: Console
  url: https://cloud.oracle.com/integration
- title: OCI SDKs
  type: SDK
  url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
- title: OCI CLI
  type: CLI
  url: https://github.com/oracle/oci-cli
- title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- title: OCI CLI Repository
  type: GitHubRepository
  url: https://github.com/oracle/oci-cli
- title: Python SDK Repository
  type: GitHubRepository
  url: https://github.com/oracle/oci-python-sdk
- title: Go SDK Repository
  type: GitHubRepository
  url: https://github.com/oracle/oci-go-sdk
- title: ''
  type: Training
  url: https://education.oracle.com/
- title: ''
  type: Marketplace
  url: https://cloudmarketplace.oracle.com/marketplace/en_US/homeLinkPage
- title: ''
  type: SpectralRules
  url: rules/oracle-integration-spectral-rules.yml
- title: Integration Management Workflow
  type: NaftikoCapability
  url: capabilities/integration-management.yaml
- title: Developer API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/developer-api.yaml
- title: Process Automation API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/process-automation-api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/oracle-integration-vocabulary.yaml
created: '2024-01-15'
description: Oracle Integration provides native connectivity to Oracle and non-Oracle Software as a Service (SaaS) and on-premises applications, such as Oracle ERP Cloud, Oracle Service Cloud, HCM Cloud, Salesforce, Workday, EBS, SAP, NetSuite and others. It combines application integration, process automation, visual application building, and integration analytics into a single unified cloud service.
features:
- description: Library of prebuilt integration recipes and adapters for rapid deployment of common integration patterns.
  name: Prebuilt Integrations
- description: Native connectivity to Oracle SaaS, on-premises applications, and third-party services including Salesforce, SAP, Workday, and ServiceNow.
  name: Application Adapters
- description: Low-code drag-and-drop integration designer for building integration flows without extensive coding.
  name: Visual Integration Designer
- description: EDI and B2B document processing with support for trading partner management, document standards, and agreement lifecycle.
  name: B2B Document Exchange
- description: Business process management with structured and unstructured workflows, case management, and task management.
  name: Process Automation
- description: DMN-based decision model management for business rules execution and deployment.
  name: Decision Modeling
- description: Time-based scheduling of integration flows with pause, resume, start, and stop controls.
  name: Scheduled Integrations
- description: Real-time monitoring of integration instances, error tracking, activity streams, and audit records.
  name: Integration Monitoring
- description: SFTP-compliant embedded file server for file-based integration scenarios.
  name: File Server
- description: Custom adapter development framework for building reusable connectivity to proprietary or niche systems.
  name: Rapid Adapter Builder
- description: AI agent capabilities within integration projects for intelligent automation patterns and prompt templates.
  name: AI Agents
- description: ML-based guidance and recommendations for building and optimizing integrations.
  name: Machine Learning Recommendations
- description: Built-in analytics and process analytics with custom query builders and data visualization.
  name: Integration Analytics
- description: Native Fast Healthcare Interoperability Resources support for healthcare integration workflows.
  name: FHIR Support
image: /assets/icons/oracle-integration.png
integrations:
- description: Native adapter for Oracle Enterprise Resource Planning Cloud including financials, procurement, and supply chain.
  name: Oracle ERP Cloud
- description: Native adapter for Oracle Human Capital Management Cloud for HR, payroll, and talent management.
  name: Oracle HCM Cloud
- description: Native adapter for Oracle Customer Experience Cloud including sales, service, and marketing.
  name: Oracle CX Cloud
- description: Native adapter for Oracle NetSuite ERP and CRM cloud services.
  name: Oracle NetSuite
- description: Prebuilt adapter for Salesforce CRM integration with Oracle cloud and on-premises applications.
  name: Salesforce
- description: Adapter for SAP ERP and S/4HANA integration via IDoc, BAPI, and RFC protocols.
  name: SAP
- description: Prebuilt adapter for Workday HCM and financial management integration.
  name: Workday
- description: Adapter for ServiceNow ITSM and ITOM integration with Oracle applications.
  name: ServiceNow
- description: Adapter for Shopify e-commerce platform integration with order management and inventory systems.
  name: Shopify
- description: Adapter for Snowflake data warehouse integration for analytics and data pipelines.
  name: Snowflake
- description: Connectivity to Microsoft Azure services and applications for multi-cloud integration.
  name: Microsoft Azure
- description: Connectivity to Amazon Web Services for multi-cloud integration scenarios.
  name: AWS
- description: Adapter for Slack messaging integration with workflow notifications and approvals.
  name: Slack
- description: Adapter for Atlassian JIRA project management and issue tracking integration.
  name: JIRA
jsonld:
- class_count: 7
  name: Oracle Integration Developer Api Context
  property_count: 27
  slug: oracle-integration-developer-api-context
- class_count: 3
  name: Oracle Integration Process Automation Api Context
  property_count: 16
  slug: oracle-integration-process-automation-api-context
layout: provider
modified: '2026-04-18'
name: Oracle Integration
rules:
- name: Oracle Integration API Rules
  rule_count: 36
  severity_counts:
    error: 19
    hint: 0
    info: 6
    warn: 11
  slug: oracle-integration-spectral-rules
skills: []
slug: oracle-integration
solutions: []
tags:
- API Management
- Automation
- B2B Integration
- Cloud Integration
- Enterprise Integration
- Integration
- iPaaS
- Process Automation
url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/apis.yml
use_cases:
- description: Connect Oracle SaaS applications like ERP Cloud, HCM Cloud, and CX Cloud with third-party SaaS platforms.
  name: SaaS Application Integration
- description: Integrate Oracle ERP Cloud or on-premises EBS with procurement, supply chain, and financial systems.
  name: ERP Integration
- description: Synchronize human capital management data across Oracle HCM Cloud, Workday, and other HR systems.
  name: HCM Integration
- description: Automate EDI-based trading partner setup, agreement management, and document exchange.
  name: B2B Trading Partner Onboarding
- description: Automate business processes with approval workflows, case management, and task orchestration.
  name: Process Automation
- description: Build FHIR-compliant healthcare integration workflows for patient data exchange and interoperability.
  name: Healthcare Data Exchange
- description: Connect on-premises applications to Oracle Cloud and third-party cloud services via connectivity agents.
  name: Hybrid Cloud Integration
- description: Automate file transfers and processing with the embedded SFTP-compliant file server.
  name: File-Based Integration
- description: Manage integration lifecycle with export, import, and deployment APIs for DevOps automation.
  name: CI/CD For Integrations
- description: Process events and messages in real time using event-driven integration patterns and stream analytics.
  name: Real-Time Event Processing
---
