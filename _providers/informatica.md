---
api_count: 7
apis:
- description: The Informatica Intelligent Cloud Services Platform REST API provides access to platform-level resources including login and authentication, roles and privileges, user and user group management, organ
  name: Informatica Platform REST API
  slug: informatica
- description: The Data Integration REST API provides programmatic access to manage data integration assets and operations, including connections, mappings, mapping tasks, dynamic mapping tasks, taskflows, code task
  name: Informatica Data Integration REST API
  slug: data-integration-rest-api
- description: 'The Cloud Data Governance and Catalog API enables programmatic creation and management of assets, searching for assets, and viewing asset details within Informatica Data Governance and Catalog. Calls '
  name: Informatica Cloud Data Governance and Catalog API
  slug: cloud-data-governance-and-catalog-api
- description: The Cloud Data Profiling REST API allows interaction with the Data Profiling Service through API calls to create, delete, update, and run queries and profiles within your organization. Supports platfo
  name: Informatica Cloud Data Profiling REST API
  slug: cloud-data-profiling-rest-api
- description: The Cloud Address Verification API is a REST API-based solution for verifying and validating postal addresses in real time. You can integrate the Address Verification service API endpoints into your a
  name: Informatica Cloud Address Verification API
  slug: cloud-address-verification-api
- description: The B2B Gateway REST APIs enable running inbound and outbound partner flows, querying the status of events, and getting control numbers for outbound EDI X12 and EDIFACT messages through programmatic A
  name: Informatica B2B Gateway REST API
  slug: b2b-gateway-rest-api
- description: 'The Reference 360 REST API enables programmatic management of reference data, including exporting and importing reference data sets, managing code values and value mappings, retrieving asset details, '
  name: Informatica Reference 360 REST API
  slug: reference-360-rest-api
capabilities:
- description: Unified workflow for managing data integration pipelines including connections, mappings, mapping tasks, job execution, scheduling, and activity monitoring. Used by data engineers and ETL developers.
  name: Informatica Data Integration
  slug: data-integration
common:
- title: ''
  type: Portal
  url: https://developer.informatica.com/
- title: ''
  type: Documentation
  url: https://docs.informatica.com/
- title: ''
  type: KnowledgeCenter
  url: https://knowledge.informatica.com/
- title: ''
  type: Support
  url: https://www.informatica.com/support.html
- title: Community
  type: Support
  url: https://network.informatica.com/
- title: ''
  type: Login
  url: https://dm-us.informaticacloud.com/identity-service/home
- title: ''
  type: SpectralRules
  url: rules/informatica-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/informatica-vocabulary.yaml
- title: Platform REST API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/platform-rest-api.yaml
- title: Data Integration Workflow
  type: NaftikoCapability
  url: capabilities/data-integration.yaml
created: '2025-01-08'
description: Collection of APIs for Informatica Intelligent Cloud Services (IICS) and Intelligent Data Management Cloud (IDMC), providing programmatic access to data integration, data governance, data quality, master data management, B2B gateway, and platform administration capabilities.
features:
- description: Connect, transform, and move data across cloud and on-premises environments using visual mapping interfaces.
  name: Data Integration
- description: Discover, catalog, and govern data assets with automated classification and lineage tracking.
  name: Data Governance
- description: Profile, cleanse, standardize, and validate data to ensure accuracy and consistency.
  name: Data Quality
- description: Create and manage golden records for critical business entities across the enterprise.
  name: Master Data Management
- description: Validate and standardize postal addresses globally in real time.
  name: Address Verification
- description: Exchange EDI documents with trading partners using X12, EDIFACT, and other B2B protocols.
  name: B2B Gateway
- description: Manage code lists, crosswalks, and hierarchies for standardized reference data across systems.
  name: Reference Data Management
- description: Build and manage API-led integrations connecting SaaS, cloud, and on-premises applications.
  name: API and Application Integration
image: https://companieslogo.com/img/orig/INFA-3e1d4e5a.png
integrations:
- description: Native connectors for bidirectional data integration with Salesforce CRM and platform.
  name: Salesforce
- description: Pre-built connectors for SAP ERP, S/4HANA, and SAP BW data integration.
  name: SAP
- description: Optimized connectors for loading, transforming, and managing data in Snowflake.
  name: Snowflake
- description: Native connectors for S3, Redshift, DynamoDB, and other AWS data services.
  name: Amazon Web Services
- description: Connectors for Azure SQL, Blob Storage, Synapse Analytics, and other Azure services.
  name: Microsoft Azure
- description: Connectors for BigQuery, Cloud Storage, and other GCP data services.
  name: Google Cloud Platform
- description: Pre-built connectors for Workday HCM and financial data integration.
  name: Workday
- description: Connectors for ServiceNow ITSM and platform data integration.
  name: ServiceNow
jsonld:
- class_count: 0
  name: Informatica Context
  property_count: 7
  slug: informatica-context
- class_count: 0
  name: Informatica Platform Rest Context
  property_count: 0
  slug: informatica-platform-rest-context
layout: provider
modified: '2026-04-18'
name: Informatica
rules:
- name: Informatica API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: informatica-spectral-rules
skills: []
slug: informatica
solutions: []
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
url: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/apis.yml
use_cases:
- description: Extract data from multiple sources and load into cloud data warehouses like Snowflake, Redshift, or BigQuery.
  name: Cloud Data Warehouse Loading
- description: Synchronize data across CRM, ERP, and marketing platforms in real time using change data capture.
  name: Real-Time Data Synchronization
- description: Migrate data between legacy systems and modern cloud platforms with automated mapping and transformation.
  name: Data Migration
- description: Ensure data quality and governance standards to meet GDPR, CCPA, and industry-specific regulations.
  name: Regulatory Compliance
- description: Create unified customer profiles by integrating and matching data from multiple source systems.
  name: Customer 360
---
