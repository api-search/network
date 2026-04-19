---
api_count: 2
apis:
- description: REST API for centralized administration and monitoring of Teradata QueryGrid, the data fabric that enables seamless cross-system analytics. Manage data centers, systems, bridges, connectors, links, fa
  name: Teradata QueryGrid Manager API
  slug: querygrid-manager-api
- description: REST API for executing SQL queries against Teradata Vantage systems. Provides HTTP-based access to run queries, retrieve results, and manage sessions for application integration and browser-based quer
  name: Teradata Query Service API
  slug: query-service-api
capabilities:
- description: Workflow capability for managing Teradata's data fabric infrastructure. Combines QueryGrid Manager for fabric configuration with Query Service for validating cross-system connectivity. Used by data en
  name: Teradata Data Fabric Management
  slug: data-fabric-management
- description: Workflow capability for executing SQL queries and analytics against Teradata Vantage systems. Combines Query Service for SQL execution with QueryGrid for cross-system query monitoring. Used by data an
  name: Teradata Query and Analytics
  slug: query-and-analytics
common:
- title: ''
  type: Portal
  url: https://developer.teradata.com
- title: ''
  type: Documentation
  url: https://docs.teradata.com
- title: ''
  type: GettingStarted
  url: https://quickstarts.teradata.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/Teradata
- title: ''
  type: Support
  url: https://support.teradata.com
- title: ''
  type: Blog
  url: https://www.teradata.com/blog
- title: ''
  type: Training
  url: https://www.teradata.com/University
- title: ''
  type: TermsOfService
  url: https://www.teradata.com/Legal/Terms-of-Use
- title: ''
  type: PrivacyPolicy
  url: https://www.teradata.com/Legal/Privacy
- title: Python SQL Driver
  type: SDK
  url: https://pypi.org/project/teradatasql/
- title: Node.js SQL Driver
  type: SDK
  url: https://www.npmjs.com/package/teradatasql
- title: R SQL Driver
  type: SDK
  url: https://github.com/Teradata/r-driver
- title: Rust API
  type: SDK
  url: https://github.com/Teradata/teradatarustapi
- title: Go SQL Driver
  type: SDK
  url: https://github.com/Teradata/gosql-driver
- title: JDBC Driver
  type: SDK
  url: https://github.com/Teradata/jdbc-driver
- title: VS Code SQL Extension
  type: CLI
  url: https://github.com/Teradata/teradata-vscode-sql-extension
- title: MCP Server
  type: Tools
  url: https://github.com/Teradata/teradata-mcp-server
- title: QueryGrid MCP Server
  type: Tools
  url: https://github.com/Teradata/teradata-qg-mcp-server
- title: ''
  type: SpectralRules
  url: rules/teradata-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/teradata-vocabulary.yaml
- title: Data Fabric Management
  type: NaftikoCapability
  url: capabilities/data-fabric-management.yaml
- title: Query and Analytics
  type: NaftikoCapability
  url: capabilities/query-and-analytics.yaml
created: '2026-04-18'
description: Teradata provides enterprise analytics and data management solutions. The Teradata VantageCloud platform delivers connected multi-cloud data analytics with capabilities for data warehousing, advanced analytics, and machine learning at scale. Teradata offers REST APIs for managing QueryGrid data fabric connections, running SQL queries, and administering platform resources.
features:
- description: Cloud-native analytics platform available on AWS, Azure, and Google Cloud.
  name: VantageCloud
- description: Advanced analytics engine with machine learning, graph analytics, and AI capabilities built into Vantage.
  name: ClearScape Analytics
- description: Data fabric for multi-system analytics enabling queries across Teradata, Hadoop, Spark, and cloud object storage.
  name: QueryGrid
- description: Model lifecycle management for deploying, monitoring, and governing machine learning models.
  name: ModelOps
- description: On-demand AI and ML engine for exploratory analytics without infrastructure management.
  name: AI Unlimited
- description: Support for Apache Iceberg and open table formats for lakehouse analytics.
  name: Open Table Formats
image: /assets/icons/teradata.png
integrations:
- description: dbt adapter for Teradata Vantage enabling data transformations using dbt workflows.
  name: dbt
- description: Airflow provider for orchestrating Teradata data pipeline workflows.
  name: Apache Airflow
- description: Dagster integration for Teradata data orchestration and observability.
  name: Dagster
- description: Airbyte connector for ELT data pipelines to and from Teradata.
  name: Airbyte
- description: Fivetran destination connector for automated data loading into Teradata.
  name: Fivetran
- description: MuleSoft connector for integrating Teradata with enterprise application networks.
  name: MuleSoft
- description: Dataiku plugin for running analytics within the Teradata Vantage environment.
  name: Dataiku
- description: LangChain integration for using Teradata as a vector store and data source in AI applications.
  name: LangChain
- description: Teradata support for Apache Iceberg open table format for lakehouse analytics.
  name: Apache Iceberg
jsonld:
- class_count: 4
  name: Teradata Query Service Api Context
  property_count: 13
  slug: teradata-query-service-api-context
- class_count: 15
  name: Teradata Querygrid Manager Api Context
  property_count: 23
  slug: teradata-querygrid-manager-api-context
layout: provider
modified: '2026-04-18'
name: Teradata
rules:
- name: Teradata API Rules
  rule_count: 30
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 13
  slug: teradata-spectral-rules
skills: []
slug: teradata
solutions: []
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
url: https://www.teradata.com
use_cases:
- description: Centralized data warehousing with petabyte-scale analytics for enterprise reporting and BI.
  name: Enterprise Data Warehousing
- description: In-database machine learning, statistical analysis, and predictive modeling at scale.
  name: Advanced Analytics
- description: Connected analytics across AWS, Azure, and Google Cloud with data fabric integration.
  name: Multi-Cloud Analytics
- description: End-to-end machine learning model lifecycle management with ModelOps.
  name: AI and ML Operations
- description: Real-time data ingestion and analytics with QueryGrid cross-system query federation.
  name: Real-Time Data Integration
---
