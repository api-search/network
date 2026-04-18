---
api_count: 39
apis:
- description: Core REST API for managing Azure Databricks workspaces, clusters, jobs, notebooks, and other resources programmatically.
  name: Azure Databricks REST API
  slug: ''
- description: Manage Databricks clusters for running Spark jobs including creating, starting, editing, listing, terminating, and deleting clusters.
  name: Clusters API
  slug: ''
- description: Create, manage, and run jobs on Databricks clusters including scheduling, listing runs, and managing job permissions.
  name: Jobs API
  slug: ''
- description: Manage notebooks, folders, and other workspace objects including listing, importing, exporting, and deleting workspace items.
  name: Workspace API
  slug: ''
- description: Access Databricks File System (DBFS) for file operations including uploading, downloading, listing, and deleting files and directories.
  name: DBFS API
  slug: ''
- description: Manage libraries and dependencies on clusters including installing, uninstalling, and listing library statuses.
  name: Libraries API
  slug: ''
- description: Manage secrets and secret scopes for secure credential storage including creating scopes, putting secrets, and managing ACLs.
  name: Secrets API
  slug: ''
- description: Create and manage personal access tokens for API authentication including creating, listing, and revoking tokens.
  name: Token Management API
  slug: ''
- description: Manage SQL warehouses, queries, and dashboards for Databricks SQL analytics workloads.
  name: SQL Analytics API
  slug: ''
- description: Track experiments, log metrics, and manage ML models using the MLflow tracking and registry APIs.
  name: MLflow API
  slug: ''
- description: Create and manage instance pools to reduce cluster start and autoscaling times by maintaining a set of idle ready-to-use cloud instances.
  name: Instance Pools API
  slug: ''
- description: Create, list, and edit cluster policies to control cluster configurations and limit the ability to configure clusters based on a set of rules.
  name: Cluster Policies API
  slug: ''
- description: Manage Git repositories within Databricks workspaces for version control of notebooks and files.
  name: Repos API
  slug: ''
- description: Manage Git credentials for authenticating with Git providers when using Databricks Repos.
  name: Git Credentials API
  slug: ''
- description: Create, edit, delete, start, and view details about Delta Live Tables pipelines for building reliable data pipelines.
  name: Pipelines API
  slug: ''
- description: Manage permissions on workspace objects including clusters, jobs, notebooks, and other resources using access control lists.
  name: Permissions API
  slug: ''
- description: Manage Unity Catalog catalogs for organizing and governing data assets across workspaces.
  name: Unity Catalog - Catalogs API
  slug: ''
- description: Manage schemas within Unity Catalog catalogs for organizing tables, views, and functions.
  name: Unity Catalog - Schemas API
  slug: ''
- description: Manage tables within Unity Catalog schemas including listing, getting, and deleting tables.
  name: Unity Catalog - Tables API
  slug: ''
- description: Manage Unity Catalog volumes for governing non-tabular data such as files and directories.
  name: Unity Catalog - Volumes API
  slug: ''
- description: Manage permissions and grants on Unity Catalog objects including catalogs, schemas, tables, and other securable objects.
  name: Unity Catalog - Grants API
  slug: ''
- description: Manage external locations in Unity Catalog for connecting to cloud storage paths.
  name: Unity Catalog - External Locations API
  slug: ''
- description: Manage storage credentials in Unity Catalog for authenticating access to cloud storage.
  name: Unity Catalog - Storage Credentials API
  slug: ''
- description: Manage Unity Catalog metastores which serve as the top-level container for data governance.
  name: Unity Catalog - Metastores API
  slug: ''
- description: Create and manage model serving endpoints for deploying machine learning models as REST API endpoints.
  name: Model Serving Endpoints API
  slug: ''
- description: Manage registered models and model versions in the Databricks Model Registry for model lifecycle management.
  name: Model Registry API
  slug: ''
- description: Manage registered models in Unity Catalog for centralized model governance and sharing.
  name: Registered Models API
  slug: ''
- description: Manage global cluster initialization scripts that run on every cluster in the workspace.
  name: Global Init Scripts API
  slug: ''
- description: Manage IP access lists to control network access to Azure Databricks workspaces.
  name: IP Access Lists API
  slug: ''
- description: Execute SQL statements on SQL warehouses and retrieve results for programmatic SQL access.
  name: Statement Execution API
  slug: ''
- description: Execute commands on running clusters and retrieve results programmatically.
  name: Command Execution API
  slug: ''
- description: Manage files in Unity Catalog volumes and workspace filesystem with operations for uploading, downloading, and deleting files.
  name: Files API
  slug: ''
- description: Deploy and manage Databricks Apps including creating, starting, stopping, and listing custom applications.
  name: Apps API
  slug: ''
- description: Manage Lakeview dashboards programmatically including creating, updating, and publishing dashboards.
  name: Lakeview API
  slug: ''
- description: Manage online tables for low-latency serving of feature data in Unity Catalog.
  name: Online Tables API
  slug: ''
- description: Manage vector search indexes for similarity search and retrieval-augmented generation workloads.
  name: Vector Search Indexes API
  slug: ''
- description: Manage vector search endpoints for hosting vector search indexes.
  name: Vector Search Endpoints API
  slug: ''
- description: Retrieve query history for SQL warehouses including query text, status, and performance metrics.
  name: Query History API
  slug: ''
- description: Manage users, groups, and service principals across the Databricks account using SCIM 2.0 protocol.
  name: Account SCIM API
  slug: ''
capabilities:
- description: Manage Azure Databricks clusters, jobs, and workspace objects for data engineering workflows. Used by data engineers and platform administrators.
  name: Azure Databricks Data Engineering
  slug: data-engineering
common:
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/azure/databricks/getting-started/
- title: ''
  type: Pricing
  url: https://azure.microsoft.com/pricing/details/databricks/
- title: ''
  type: StatusPage
  url: https://status.azuredatabricks.net/
- title: ''
  type: Security
  url: https://learn.microsoft.com/azure/databricks/security/
- title: ''
  type: SDK
  url: https://learn.microsoft.com/azure/databricks/dev-tools/
- title: ''
  type: CLI
  url: https://learn.microsoft.com/azure/databricks/dev-tools/cli/
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/azure/databricks/dev-tools/auth/
- title: ''
  type: APIReference
  url: https://learn.microsoft.com/azure/databricks/reference/api
- title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/azure/databricks/release-notes/product/
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/azure/databricks/release-notes/
- title: ''
  type: Support
  url: https://learn.microsoft.com/answers/tags/166/azure-databricks
- title: Python SDK
  type: SDK
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-python
- title: Java SDK
  type: SDK
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-java
- title: Go SDK
  type: SDK
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-go
- title: R SDK
  type: SDK
  url: https://learn.microsoft.com/azure/databricks/dev-tools/sdk-r
- title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-databricks-client
- title: ''
  type: OpenAPI
  url: openapi/azure-databricks-openapi.yml
- title: ''
  type: JSONSchema
  url: json-schema/azure-databricks-cluster-schema.json
- title: ''
  type: JSONLD
  url: json-ld/azure-databricks-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/azure-databricks-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/azure-databricks-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-engineering.yaml
created: '2024-01-01'
description: Azure Databricks is an Apache Spark-based analytics platform optimized for Microsoft Azure. It provides a collaborative workspace for data engineers, data scientists, and analysts to work together on big data and machine learning workloads.
features:
- Collaborative notebooks with multi-language support
- Auto-scaling Apache Spark clusters
- Delta Lake for reliable data lakehouse architecture
- Unity Catalog for unified data governance
- MLflow integration for ML lifecycle management
- Model serving endpoints for real-time inference
- Delta Live Tables for declarative ETL pipelines
- SQL analytics with serverless SQL warehouses
- Vector search for RAG and similarity search
- Lakeview dashboards for data visualization
- Git integration for version control of notebooks
- SCIM 2.0 for identity and access management
image: https://azure.microsoft.com/svghandler/databricks/
integrations:
- Azure Data Factory for orchestration
- Azure Synapse Analytics for data warehousing
- Azure Data Lake Storage for scalable storage
- Azure Key Vault for secret management
- Azure Active Directory for authentication
- Power BI for business intelligence dashboards
- Terraform for infrastructure as code
- Apache Kafka for streaming data ingestion
jsonld:
- class_count: 0
  name: Azure Databricks Context
  property_count: 0
  slug: azure-databricks-context
layout: provider
modified: '2026-04-18'
name: Azure Databricks
rules:
- name: Azure Databricks API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-databricks-spectral-rules
skills: []
slug: azure-databricks
solutions: []
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
url: https://raw.githubusercontent.com/api-evangelist/azure-databricks/refs/heads/main/apis.yml
use_cases:
- Building and managing data lakehouse architectures
- Training and deploying machine learning models at scale
- Running ETL pipelines for data transformation
- Interactive data exploration and ad-hoc analytics
- Real-time streaming analytics with Structured Streaming
- Building retrieval-augmented generation (RAG) applications
- Data governance and compliance with Unity Catalog
- Collaborative data science with shared notebooks
---
