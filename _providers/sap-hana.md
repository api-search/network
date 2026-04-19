---
api_count: 13
apis:
- description: REST API for managing SAP HANA Cloud instances, monitoring, and administration.
  name: SAP HANA Cloud REST API
  slug: ''
- description: SQL interface for querying and managing data in SAP HANA databases.
  name: SAP HANA SQL API
  slug: ''
- description: Extended Application Services (XS) for building applications directly on SAP HANA.
  name: SAP HANA XS Engine API
  slug: ''
- description: RESTful API for SAP HANA Cockpit administration and monitoring.
  name: SAP HANA Cockpit API
  slug: ''
- description: APIs for data provisioning, replication, and integration.
  name: SAP HANA Smart Data Integration API
  slug: ''
- description: REST API for accessing triggered alerts, database metrics, and metering data for SAP HANA Cloud instances.
  name: SAP HANA Cloud Alerts and Metrics REST API
  slug: ''
- description: REST API providing geocoding, routing, and mapping services through a unified interface supporting multiple back-end service providers.
  name: SAP HANA Spatial Services API
  slug: ''
- description: REST API for managing, uploading, reading, deleting, and listing files in SAP HANA Cloud Data Lake file containers.
  name: SAP HANA Cloud Data Lake Files REST API
  slug: ''
- description: API for managing HDI containers used to deploy database artifacts in isolated schemas with dependency management and lifecycle support.
  name: SAP HANA Deployment Infrastructure (HDI) API
  slug: ''
- description: In-database machine learning and statistical algorithms library providing clustering, classification, regression, and time series analysis capabilities.
  name: SAP HANA Predictive Analysis Library (PAL) API
  slug: ''
- description: API for storing, querying, and managing semi-structured JSON documents within SAP HANA using a hybrid relational and document-oriented approach.
  name: SAP HANA JSON Document Store API
  slug: ''
- description: Graph processing engine for network analysis with built-in algorithms for path finding, pattern matching, and knowledge graph capabilities using OpenCypher and SPARQL.
  name: SAP HANA Graph Engine API
  slug: ''
- description: REST API for retrieving system information and metadata about SAP HANA Platform instances.
  name: SAP HANA REST Info API
  slug: ''
capabilities:
- description: Unified workflow for SAP HANA Cloud database administration including instance lifecycle management, monitoring alerts, performance metrics, and metering. Used by database administrators and cloud pla
  name: SAP HANA Cloud Administration
  slug: cloud-administration
common:
- title: ''
  type: DeveloperPortal
  url: https://api.sap.com/
- title: ''
  type: Support
  url: https://support.sap.com/
- title: ''
  type: Pricing
  url: https://www.sap.com/products/technology-platform/hana/pricing.html
- title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- title: ''
  type: TermsOfService
  url: https://www.sap.com/about/trust-center/agreements.html
- title: ''
  type: GettingStarted
  url: https://www.sap.com/products/data-cloud/hana/get-started.html
- title: ''
  type: Tutorials
  url: https://developers.sap.com/tutorial-navigator.html
- title: ''
  type: GitHubRepository
  url: https://github.com/SAP-samples
- title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- title: ''
  type: JSONLD
  url: json-ld/sap-hana-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/sap-hana-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/cloud-administration.yaml
created: '2024-01-01'
description: APIs for SAP HANA, an in-memory, column-oriented, relational database management system developed and marketed by SAP SE.
features:
- description: Process massive datasets in real-time using columnar in-memory storage for analytics and transactions.
  name: In-Memory Computing
- description: Support for relational, graph, spatial, JSON document, and time series data in a single database.
  name: Multi-Model Processing
- description: Fully managed cloud database service with elastic scaling, automated backups, and multi-region deployment.
  name: Cloud Native
- description: Built-in machine learning algorithms through the Predictive Analysis Library for in-database analytics.
  name: Predictive Analytics
- description: Seamlessly extend storage with SAP HANA Cloud Data Lake for cost-effective warm and cold data management.
  name: Data Lake Integration
- description: Real-time and batch data replication from heterogeneous sources with built-in data quality.
  name: Smart Data Integration
image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
integrations:
- description: Native integration with SAP Business Technology Platform for enterprise application development.
  name: SAP BTP
- description: Serve as the underlying database for SAP S/4HANA ERP suite.
  name: SAP S/4HANA
- description: Direct live connections for real-time business intelligence dashboards and planning.
  name: SAP Analytics Cloud
- description: Deploy SAP HANA Cloud instances on Azure infrastructure with cross-cloud governance.
  name: Microsoft Azure
jsonld:
- class_count: 0
  name: Sap Hana Cloud Rest Context
  property_count: 0
  slug: sap-hana-cloud-rest-context
- class_count: 0
  name: Sap Hana Context
  property_count: 14
  slug: sap-hana-context
layout: provider
modified: '2026-04-18'
name: SAP HANA
rules:
- name: SAP HANA API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: sap-hana-spectral-rules
skills: []
slug: sap-hana
solutions: []
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
url: https://www.sap.com/products/technology-platform/hana.html
use_cases:
- description: Run complex analytical queries on live transactional data without ETL delays.
  name: Real-Time Analytics
- description: Build high-performance applications directly on the database using XS Engine and HDI containers.
  name: Application Development
- description: Ingest and analyze high-volume sensor and device data with time series and spatial capabilities.
  name: IoT Data Processing
- description: Consolidate enterprise data for reporting and business intelligence with columnar compression.
  name: Enterprise Data Warehousing
---
