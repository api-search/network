---
api_count: 57
apis:
- description: Databricks is a cloud-based data platform that simplifies and accelerates the process of preparing and analyzing large volumes of data. The platform integrates with popular data sources and tools, all
  name: Databricks
  slug: databricks
- description: The Databricks Clusters API allows you to create, start, edit, list, terminate, and delete clusters. Clusters are managed cloud resources that enable you to run data engineering and data science workl
  name: Databricks Clusters API
  slug: clusters-api
- description: The Databricks Jobs API allows you to create, edit, delete, and trigger jobs. Jobs are the primary mechanism for running automated workloads on Databricks, including notebooks, JARs, Python scripts, a
  name: Databricks Jobs API
  slug: jobs-api
- description: The Databricks File System (DBFS) API is a distributed file system mounted into a Databricks workspace and available on Databricks clusters. The API enables you to interact with object storage using d
  name: Databricks DBFS API
  slug: dbfs-api
- description: The Databricks Workspace API allows you to list, import, export, and delete notebooks, folders, and libraries in a Databricks workspace. It provides programmatic access to manage workspace objects, en
  name: Databricks Workspace API
  slug: workspace-api
- description: The Databricks SQL Warehouses API allows you to create, edit, list, start, stop, and delete SQL warehouses. SQL warehouses are compute resources that enable you to run SQL commands on data objects wit
  name: Databricks SQL Warehouses API
  slug: sql-warehouses-api
- description: The Databricks Pipelines API allows you to create, edit, delete, start, and stop Delta Live Tables pipelines. Delta Live Tables is a declarative framework for building reliable, maintainable, and test
  name: Databricks Pipelines API
  slug: pipelines-api
- description: The Databricks Serving Endpoints API allows you to create, update, query, and delete model serving endpoints. Mosaic AI Model Serving provides a unified interface to deploy, govern, and query AI model
  name: Databricks Serving Endpoints API
  slug: serving-endpoints-api
- description: The Databricks Secrets API allows you to manage secrets, secret scopes, and secret ACLs. Secrets provide a secure way to store and reference credentials and other sensitive information in notebooks an
  name: Databricks Secrets API
  slug: secrets-api
- description: The Databricks Instance Pools API allows you to create, edit, delete, and list instance pools. Instance pools reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use clo
  name: Databricks Instance Pools API
  slug: instance-pools-api
- description: The Databricks Token Management API enables workspace administrators to manage personal access tokens for users and service principals. It allows creating, listing, and revoking tokens, providing cent
  name: Databricks Token Management API
  slug: token-management-api
- description: The Databricks Catalogs API is part of Unity Catalog and allows you to create, update, list, and delete catalogs. Catalogs are the top-level container for data objects in Unity Catalog, providing a th
  name: Databricks Catalogs API
  slug: catalogs-api
- description: The Databricks Vector Search Indexes API allows you to create, manage, query, and delete vector search indexes. Vector Search enables you to store vector representations of your data and perform simil
  name: Databricks Vector Search Indexes API
  slug: vector-search-indexes-api
- description: The Databricks Model Versions API allows you to manage model versions within the Unity Catalog model registry. It provides programmatic access to create, update, list, and delete model versions, enabl
  name: Databricks Model Versions API
  slug: model-versions-api
- description: The Databricks Permissions API allows you to manage permissions on workspace objects such as clusters, jobs, notebooks, and SQL warehouses. It provides programmatic access to get, set, and update acce
  name: Databricks Permissions API
  slug: permissions-api
- description: The Databricks Repos API allows you to manage Git repositories within a Databricks workspace. It provides programmatic access to create, update, delete, and list repos, as well as perform Git operatio
  name: Databricks Repos API
  slug: repos-api
- description: The Databricks Git Credentials API allows you to manage Git credentials for authenticating with Git providers. It provides programmatic access to create, update, delete, and list stored Git credential
  name: Databricks Git Credentials API
  slug: git-credentials-api
- description: The Databricks Cluster Policies API allows administrators to create, edit, delete, and list cluster policies. Cluster policies limit the ability to configure clusters based on a set of rules, enabling
  name: Databricks Cluster Policies API
  slug: cluster-policies-api
- description: The Databricks Libraries API allows you to install, uninstall, and list libraries on clusters. It provides programmatic management of Python, Java, Scala, and R library dependencies for cluster worklo
  name: Databricks Libraries API
  slug: libraries-api
- description: The Databricks Global Init Scripts API enables workspace administrators to manage global initialization scripts that run on every cluster in the workspace. It provides programmatic access to create, u
  name: Databricks Global Init Scripts API
  slug: global-init-scripts-api
- description: The Databricks Command Execution API allows you to execute Python, Scala, SQL, or R commands on running Databricks clusters. It provides programmatic access to create execution contexts, run commands,
  name: Databricks Command Execution API
  slug: command-execution-api
- description: The Databricks Statement Execution API allows you to execute SQL statements on Databricks SQL warehouses and retrieve results. It provides a synchronous and asynchronous interface for running SQL quer
  name: Databricks Statement Execution API
  slug: statement-execution-api
- description: The Databricks Queries API allows you to create, update, delete, list, and run saved SQL queries in Databricks SQL. It provides programmatic management of SQL query objects, enabling automation of ana
  name: Databricks Queries API
  slug: queries-api
- description: The Databricks Alerts API allows you to create, update, delete, and list alerts in Databricks SQL. Alerts automate query execution, evaluate custom conditions, and deliver notifications when those con
  name: Databricks Alerts API
  slug: alerts-api
- description: The Databricks Schemas API is part of Unity Catalog and allows you to create, update, list, and delete schemas. Schemas, also known as databases, reside within catalogs and contain tables, views, volu
  name: Databricks Schemas API
  slug: schemas-api
- description: 'The Databricks Tables API is part of Unity Catalog and allows you to create, update, list, and delete tables. Tables reside within schemas and represent structured data assets, supporting managed and '
  name: Databricks Tables API
  slug: tables-api
- description: The Databricks Volumes API is part of Unity Catalog and allows you to create, update, list, and delete volumes. Volumes provide a governed location for storing and accessing non-tabular data files suc
  name: Databricks Volumes API
  slug: volumes-api
- description: The Databricks Functions API is part of Unity Catalog and allows you to create, list, and delete user-defined functions. Functions reside within schemas and can be used in SQL queries and notebooks, w
  name: Databricks Functions API
  slug: functions-api
- description: The Databricks Grants API is part of Unity Catalog and allows you to get, update, and manage permissions on Unity Catalog securable objects. It provides programmatic control over access to catalogs, s
  name: Databricks Grants API
  slug: grants-api
- description: The Databricks External Locations API is part of Unity Catalog and allows you to create, update, list, and delete external locations. External locations combine a cloud storage path with a storage cre
  name: Databricks External Locations API
  slug: external-locations-api
- description: The Databricks Storage Credentials API is part of Unity Catalog and allows you to create, update, list, and delete storage credentials. Storage credentials contain long-term cloud credentials that pro
  name: Databricks Storage Credentials API
  slug: storage-credentials-api
- description: The Databricks Metastores API is part of Unity Catalog and allows you to create, update, list, and delete metastores. A metastore is the top-level container of objects in Unity Catalog, providing cent
  name: Databricks Metastores API
  slug: metastores-api
- description: The Databricks Connections API is part of Unity Catalog and allows you to create, update, list, and delete connections to external data sources. Connections enable federated queries across external da
  name: Databricks Connections API
  slug: connections-api
- description: The Databricks Registered Models API allows you to create, update, list, and delete registered models in the Unity Catalog model registry. It provides centralized model lifecycle management with versi
  name: Databricks Registered Models API
  slug: registered-models-api
- description: The Databricks Experiments API allows you to create, update, list, and manage MLflow experiments. Experiments are the primary unit of organization in MLflow, grouping runs that track parameters, metri
  name: Databricks Experiments API
  slug: experiments-api
- description: The Databricks Online Tables API allows you to create, get, and delete online tables. Online tables are materialized copies of Delta tables optimized for low-latency lookups, enabling real-time featur
  name: Databricks Online Tables API
  slug: online-tables-api
- description: The Databricks Quality Monitors API allows you to create, update, get, and delete data quality monitors for tables. Quality monitors enable automated data profiling and anomaly detection, providing co
  name: Databricks Quality Monitors API
  slug: quality-monitors-api
- description: 'The Databricks Vector Search Endpoints API allows you to create, list, get, and delete vector search endpoints. Vector search endpoints are compute resources that host vector search indexes, enabling '
  name: Databricks Vector Search Endpoints API
  slug: vector-search-endpoints-api
- description: The Databricks Shares API is part of Delta Sharing and allows you to create, update, list, and delete shares. A share is a read-only logical collection of tables and table partitions that a data provi
  name: Databricks Shares API
  slug: shares-api
- description: The Databricks Recipients API is part of Delta Sharing and allows you to create, update, list, and delete recipients. A recipient is an entity that receives shared data from a provider, and can be eit
  name: Databricks Recipients API
  slug: recipients-api
- description: The Databricks Providers API is part of Delta Sharing and allows you to create, update, list, and delete data providers. Providers represent organizations that share data through Delta Sharing, enabli
  name: Databricks Providers API
  slug: providers-api
- description: The Databricks Clean Rooms API allows you to create, update, list, and delete clean rooms. Clean rooms use Delta Sharing and serverless compute to provide a secure and privacy-protecting environment w
  name: Databricks Clean Rooms API
  slug: clean-rooms-api
- description: The Databricks Notification Destinations API allows you to create, update, list, and delete notification destinations for a workspace. Notification destinations define where alerts and notifications a
  name: Databricks Notification Destinations API
  slug: notification-destinations-api
- description: The Databricks Apps API allows you to create, deploy, manage, and delete Databricks Apps. Apps run directly on a Databricks workspace, integrating with workspace data and services to build custom data
  name: Databricks Apps API
  slug: apps-api
- description: The Databricks Lakeview API allows you to create, update, get, list, and delete AI/BI dashboards. Lakeview dashboards provide a modern visualization experience built on top of Databricks SQL, enabling
  name: Databricks Lakeview API
  slug: lakeview-api
- description: The Databricks Files API provides a standard HTTP interface for reading, writing, listing, and deleting files and directories in Unity Catalog volumes and other workspace storage locations. It support
  name: Databricks Files API
  slug: files-api
- description: The Databricks Tokens API allows you to create, list, and revoke personal access tokens. Personal access tokens are used to authenticate with the Databricks REST API and integrations, providing an alt
  name: Databricks Tokens API
  slug: tokens-api
- description: The Databricks IP Access Lists API allows administrators to configure IP allow lists and block lists for a workspace. It provides programmatic management of network security rules to restrict access t
  name: Databricks IP Access Lists API
  slug: ip-access-lists-api
- description: 'The Databricks Current User API allows you to retrieve information about the currently authenticated user or service principal. It returns identity details including username, display name, and group '
  name: Databricks Current User API
  slug: current-user-api
- description: The Databricks Groups API allows you to create, update, list, and delete groups in a workspace. Groups simplify identity management by enabling administrators to assign access permissions to collectio
  name: Databricks Groups API
  slug: groups-api
- description: 'The Databricks Service Principals API allows you to create, update, list, and delete service principals in a workspace. Service principals are identities for automated tools, jobs, scripts, apps, and '
  name: Databricks Service Principals API
  slug: service-principals-api
- description: The Databricks Users API allows you to create, update, list, and delete users in a workspace. It provides programmatic management of user identities and their workspace access, supporting SCIM protoco
  name: Databricks Users API
  slug: users-api
- description: The Databricks Dashboards API allows you to create, update, list, and delete legacy SQL dashboards. Dashboards provide visual representations of query results, enabling business intelligence reporting
  name: Databricks Dashboards API
  slug: dashboards-api
- description: The Databricks Model Registry API provides the workspace model registry for managing the full lifecycle of ML models. It enables creating registered models, managing model versions, transitioning stag
  name: Databricks Model Registry API
  slug: model-registry-api
- description: The Databricks Workspace Bindings API allows you to manage the binding of Unity Catalog securables to specific workspaces. It enables configuring whether catalogs and other objects are available acros
  name: Databricks Workspace Bindings API
  slug: workspace-bindings-api
- description: The Databricks System Schemas API allows you to enable, disable, and list system schemas within a metastore. System schemas contain system tables that provide operational data about your Databricks ac
  name: Databricks System Schemas API
  slug: system-schemas-api
- description: 'The Databricks Table Constraints API allows you to create and delete primary key and foreign key constraints on Unity Catalog tables. Table constraints define relationships between tables, supporting '
  name: Databricks Table Constraints API
  slug: table-constraints-api
capabilities:
- description: Unified workflow for Databricks data engineering including cluster management, job orchestration, and workspace operations. Used by data engineers and platform administrators.
  name: Databricks Data Engineering
  slug: data-engineering
common:
- title: ''
  type: Authentication
  url: https://docs.databricks.com/dev-tools/auth.html
- title: ''
  type: Getting Started
  url: https://docs.databricks.com/getting-started/index.html
- title: ''
  type: SDKs
  url: https://docs.databricks.com/dev-tools/sdks.html
- title: ''
  type: StatusPage
  url: https://status.databricks.com/
- title: ''
  type: Support
  url: https://help.databricks.com/
- title: ''
  type: API Reference
  url: https://docs.databricks.com/api/workspace/introduction
- title: ''
  type: Documentation
  url: https://docs.databricks.com/aws/en/reference/api
- title: ''
  type: Pricing
  url: https://www.databricks.com/product/pricing
- title: ''
  type: Sign Up
  url: https://www.databricks.com/try-databricks
- title: ''
  type: PrivacyPolicy
  url: https://www.databricks.com/legal/privacynotice
- title: ''
  type: TermsOfService
  url: https://www.databricks.com/legal/terms-of-use
- title: ''
  type: Security
  url: https://www.databricks.com/trust
- title: ''
  type: RateLimits
  url: https://docs.databricks.com/aws/en/resources/limits
- title: ''
  type: ChangeLog
  url: https://docs.databricks.com/aws/en/release-notes/
- title: ''
  type: Blog
  url: https://www.databricks.com/blog
- title: Community Forum
  type: Support
  url: https://community.databricks.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/databricks
- title: Python SDK
  type: SDK
  url: https://github.com/databricks/databricks-sdk-py
- title: Go SDK
  type: SDK
  url: https://github.com/databricks/databricks-sdk-go
- title: ''
  type: CLI
  url: https://github.com/databricks/cli
- title: ''
  type: Documentation
  url: https://docs.databricks.com/aws/en/dev-tools/cli
- title: ''
  type: X
  url: https://twitter.com/databricks
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/databricks
- title: ''
  type: Login
  url: https://login.databricks.com/
- title: ''
  type: Contact
  url: https://www.databricks.com/company/contact
- title: ''
  type: Training
  url: https://www.databricks.com/learn/training/home
- title: ''
  type: Academy
  url: https://customer-academy.databricks.com/learn
- title: Java SDK
  type: SDK
  url: https://github.com/databricks/databricks-sdk-java
- title: Python SQL SDK
  type: SDK
  url: https://github.com/databricks/databricks-sql-python
- title: Terraform Provider
  type: SDK
  url: https://github.com/databricks/terraform-provider-databricks
- title: MLflow API Reference
  type: APIReference
  url: https://docs.databricks.com/aws/en/reference/mlflow-api
- title: ''
  type: Security
  url: https://www.databricks.com/trust/security-features
- title: ''
  type: Authentication
  url: https://docs.databricks.com/aws/en/dev-tools/auth
- title: ''
  type: APIReference
  url: https://api-docs.databricks.com/
- title: ''
  type: OpenAPI
  url: openapi/databricks-openapi.yml
- title: ''
  type: JSONSchema
  url: json-schema/databricks-cluster-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/databricks-job-schema.json
- title: ''
  type: JSONLD
  url: json-ld/databricks-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/databricks-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-engineering.yaml
created: '2025-01-14'
description: Collection of Databricks REST APIs for managing workspaces, clusters, jobs, and data operations.
features:
- description: Combine data warehousing and data lake capabilities in a single, open platform built on Delta Lake.
  name: Unified Data Lakehouse
- description: Auto-scaling serverless SQL warehouses and compute that eliminate infrastructure management.
  name: Serverless Compute
- description: Unified governance for data and AI assets with fine-grained access control and lineage tracking.
  name: Unity Catalog
- description: Declarative ETL framework for building reliable, maintainable data processing pipelines.
  name: Delta Live Tables
- description: Integrated AI platform for building, deploying, and monitoring machine learning and generative AI models.
  name: Mosaic AI
- description: Built-in vector similarity search for RAG applications and AI-powered retrieval.
  name: Vector Search
- description: Open protocol for secure cross-organization data sharing without data copying.
  name: Delta Sharing
image: https://www.databricks.com/en-website-assets/static/f9f2b15ae456c41f7d2e5b303c8c6c6e/databricks-logo.svg
integrations:
- description: Native integration with Apache Spark for distributed data processing at scale.
  name: Apache Spark
- description: Built on Delta Lake open format for ACID transactions and time travel on data lakes.
  name: Delta Lake
- description: Open-source platform for managing the complete machine learning lifecycle.
  name: MLflow
- description: Infrastructure-as-code provider for automating Databricks workspace provisioning.
  name: Terraform
- description: Integration with dbt for SQL-based data transformation workflows.
  name: dbt
jsonld:
- class_count: 0
  name: Databricks Context
  property_count: 0
  slug: databricks-context
layout: provider
modified: '2026-04-18'
name: Databricks
rules:
- name: Databricks API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: databricks-spectral-rules
skills: []
slug: databricks
solutions: []
tags:
- AI
- Analytics
- Apache Spark
- Big Data
- Clean Rooms
- Cloud Computing
- Data
- Data Analytics
- Data Engineering
- Data Governance
- Delta Lake
- Delta Sharing
- ETL
- Identity Management
- Lakehouse
- Machine Learning
- MLflow
- Model Serving
- Security
- SQL
- Unity Catalog
- Vector Search
- Visualize
url: https://raw.githubusercontent.com/api-evangelist/databricks/refs/heads/main/apis.yml
use_cases:
- description: Build and orchestrate ETL pipelines with Delta Live Tables and multi-task workflows.
  name: Data Engineering
- description: Run analytical SQL queries on lakehouse data with serverless SQL warehouses.
  name: Data Warehousing
- description: Train, track, and deploy ML models with MLflow experiment tracking and model registry.
  name: Machine Learning
- description: Process streaming data with structured streaming and serve results through online tables.
  name: Real-Time Analytics
- description: Govern data assets across the organization with Unity Catalog metadata management.
  name: Data Governance
---
