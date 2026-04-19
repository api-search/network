---
api_count: 1
apis:
- description: Airbyte is an open-source data integration platform that enables businesses to move and consolidate data from various sources into centralized destinations. The Airbyte API provides programmatic contr
  name: Airbyte
  slug: airbyte
capabilities:
- description: Unified workflow capability for managing Airbyte data integration pipelines — sources, destinations, connections, and sync jobs. Used by data engineers and platform teams.
  name: Airbyte Data Pipeline Management
  slug: data-pipeline-management
common:
- title: ''
  type: Portal
  url: https://airbyte.com
- title: ''
  type: Console
  url: https://cloud.airbyte.io
- title: ''
  type: SignUp
  url: https://cloud.airbyte.io
- title: ''
  type: Pricing
  url: https://airbyte.com/pricing
- title: ''
  type: GitHubOrganization
  url: https://github.com/airbytehq
- title: ''
  type: GitHubRepository
  url: https://github.com/airbytehq/airbyte
- title: ''
  type: GettingStarted
  url: https://docs.airbyte.com
- title: ''
  type: StatusPage
  url: https://status.airbyte.com
- title: ''
  type: Blog
  url: https://airbyte.com/blog
- title: ''
  type: Tutorials
  url: https://airbyte.com/tutorials
- title: ''
  type: Support
  url: https://support.airbyte.com/hc/en-us
- title: ''
  type: PrivacyPolicy
  url: https://airbyte.com/company/privacy-policy
- title: ''
  type: TermsOfService
  url: https://airbyte.com/company/terms
- title: ''
  type: Newsletter
  url: https://airbyte.com/community/newsletter
- title: ''
  type: ChangeLog
  url: https://docs.airbyte.com/category/release-notes/
- title: ''
  type: RoadMap
  url: https://github.com/orgs/airbytehq/projects/37/views/1
- title: PyAirbyte
  type: SDK
  url: https://github.com/airbytehq/PyAirbyte
- title: Airbyte CLI (abctl)
  type: CLI
  url: https://github.com/airbytehq/abctl
- title: Python Connector CDK
  type: SDK
  url: https://github.com/airbytehq/airbyte-python-cdk
- title: Agent SDK
  type: SDK
  url: https://github.com/airbytehq/airbyte-agent-sdk
- title: Helm Chart
  type: SDK
  url: https://artifacthub.io/packages/helm/airbyte/airbyte
- title: Airbyte Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/rules/airbyte-spectral-rules.yml
- title: Data Pipeline Management
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/capabilities/data-pipeline-management.yaml
- title: Airbyte Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/vocabulary/airbyte-vocabulary.yaml
created: '2025-01-08'
description: Airbyte is an open-source data integration platform that enables businesses to easily and efficiently move and consolidate their data from various sources into one centralized location. With Airbyte, organizations can seamlessly connect and synchronize data from sources such as databases, APIs, and other third-party applications, allowing for real-time insights and analysis. Airbyte offers both self-hosted and cloud-hosted options, with a catalog of hundreds of pre-built connectors.
features:
- description: Connect and sync data from hundreds of sources to destinations.
  name: Data Integration
- description: Self-host Airbyte on your own infrastructure with full access to source code.
  name: Open Source
- description: Managed cloud offering with 30-day free trial at cloud.airbyte.io.
  name: Cloud Hosted
- description: Pre-built connectors for databases, APIs, SaaS tools, and data warehouses.
  name: Connector Catalog
- description: Build custom connectors using the Python CDK or low-code/no-code builder.
  name: Custom Connectors
- description: Airbyte Agent SDK provides AI agents with reliable, permission-aware access to data sources.
  name: AI Agent Integration
- description: Manage Airbyte infrastructure and connections as code with Terraform.
  name: Terraform Support
- description: Model Context Protocol support for integration with AI tools.
  name: MCP Servers
- description: Embed Airbyte connector UI into your own product for white-label data integration.
  name: Embedded Widget
- description: Python library for using Airbyte connectors programmatically in Python environments.
  name: PyAirbyte
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Orchestrate Airbyte syncs from Airflow DAGs.
  name: Apache Airflow
- description: Transform data after Airbyte syncs with dbt models.
  name: dbt
- description: Load data into Snowflake data warehouse.
  name: Snowflake
- description: Sync data to Google BigQuery.
  name: BigQuery
- description: Load data into Amazon Redshift.
  name: Redshift
- description: Ingest data into Databricks lakehouse.
  name: Databricks
- description: Infrastructure-as-code support for Airbyte resources.
  name: Terraform
- description: Deploy Airbyte on Kubernetes using official Helm charts.
  name: Kubernetes / Helm
jsonld:
- class_count: 108
  name: Airbyte Context
  property_count: 129
  slug: airbyte-context
layout: provider
modified: '2026-04-19'
name: Airbyte
rules:
- name: Airbyte API Rules
  rule_count: 28
  severity_counts:
    error: 9
    hint: 0
    info: 7
    warn: 12
  slug: airbyte-spectral-rules
skills: []
slug: airbyte
solutions: []
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/apis.yml
use_cases:
- description: Sync operational data to Snowflake, BigQuery, Redshift, or other warehouses.
  name: Data Warehouse Loading
- description: Land raw data into S3, GCS, or Azure data lakes.
  name: Data Lake Ingestion
- description: Build ELT pipelines for business intelligence and analytics.
  name: Analytics Pipelines
- description: Aggregate training data from multiple sources for machine learning.
  name: AI/ML Data Preparation
- description: Pull data from SaaS APIs (Salesforce, HubSpot, Stripe) into your data stack.
  name: API Data Sync
- description: Replicate relational databases with CDC change data capture.
  name: Database Replication
- description: Load and embed data into vector stores for AI search and retrieval.
  name: Vector Database Population
---
