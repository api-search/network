---
api_count: 4
apis:
- description: REST API for managing data sources, schemas, tables, columns, and custom field values in the Alation data catalog. Supports metadata retrieval and batch updates for catalog objects.
  name: Alation Data Catalog API
  slug: data-catalog-api
- description: REST API for managing data lineage and dataflow objects in Alation. Supports creating, retrieving, updating, and deleting lineage paths between catalog objects.
  name: Alation Lineage API
  slug: lineage-api
- description: REST API for data governance workflows in Alation, including business glossary management, governance policy enforcement, and data quality rules and scoring.
  name: Alation Governance API
  slug: governance-api
- description: REST API for searching and discovering catalog assets in Alation. Supports full-text search, AI-powered aggregated context retrieval, and article browsing.
  name: Alation Search API
  slug: search-api
capabilities:
- description: Workflow capability for data intelligence operations combining catalog search, lineage tracking, governance, and metadata management in the Alation platform. Enables data stewards, analysts, and AI ag
  name: Alation Data Intelligence
  slug: data-intelligence
common:
- title: ''
  type: Website
  url: https://alation.com
- title: ''
  type: Documentation
  url: https://developer.alation.com
- title: ''
  type: GettingStarted
  url: https://developer.alation.com/dev/docs/about-the-alation-apis
- title: ''
  type: GitHubOrganization
  url: https://github.com/Alation
- title: ''
  type: SpectralRules
  url: rules/alation-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/alation-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/alation-alation-context.jsonld
- title: Alation Data Catalog Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/data-catalog-api.yaml
- title: Alation Lineage Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/lineage-api.yaml
- title: Alation Governance Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/governance-api.yaml
- title: Alation Search Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/search-api.yaml
- title: Data Intelligence Workflow
  type: NaftikoCapability
  url: capabilities/data-intelligence.yaml
created: '2025-01-08'
description: Alation is a data intelligence platform that helps organizations harness the power of their data by providing a centralized platform for data cataloging, governance, and collaboration. By enabling users to easily search, understand, and trust their data, Alation empowers organizations to make data-driven decisions with confidence. Through advanced analytics and AI capabilities, Alation helps organizations uncover insights, improve data quality, and drive innovation.
features:
- description: Centralized catalog for data sources, schemas, tables, and columns with rich metadata, descriptions, and custom fields for discoverability.
  name: Data Catalog
- description: End-to-end data lineage tracking via dataflow objects showing how data moves between sources, transformations, and targets.
  name: Data Lineage
- description: Collaborative business glossary for defining standardized terms, abbreviations, and synonyms with stewardship assignments.
  name: Business Glossary
- description: Comprehensive data quality rules covering accuracy, completeness, consistency, timeliness, uniqueness, validity, and custom dimensions.
  name: Data Quality
- description: Governance policy management for data protection, retention, access control, and quality enforcement across the enterprise.
  name: Governance Policies
- description: Full-text and semantic search powered by AI for discovering trusted data assets, with aggregated context for LLM consumption.
  name: AI-Powered Search
- description: Specialized API for AI applications to retrieve structured catalog context for natural language queries, enabling RAG and AI agent workflows.
  name: Aggregated Context API
- description: Extensible metadata framework with custom fields for any catalog object type, supporting batch updates via the REST API.
  name: Custom Fields
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native Snowflake integration for automatic metadata harvesting and query log analysis to build comprehensive data lineage.
  name: Snowflake
- description: dbt integration for capturing transformation lineage and linking dbt models to physical tables in the Alation catalog.
  name: dbt
- description: BI metadata integration for cataloging Tableau reports and dashboards with lineage to underlying data sources.
  name: Tableau
- description: Official Python SDK and AI Agent SDK for programmatic access to Alation catalog APIs and AI agent development.
  name: Python SDK
- description: Integration with Apache Atlas for federated metadata management across heterogeneous data platforms.
  name: Apache Atlas
jsonld:
- class_count: 0
  name: Alation Alation Context
  property_count: 60
  slug: alation-alation-context
layout: provider
modified: '2026-04-19'
name: Alation
rules:
- name: Alation API Rules
  rule_count: 26
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 10
  slug: alation-spectral-rules
skills: []
slug: alation
solutions: []
tags:
- Data Catalog
- Data Governance
- Data Intelligence
- Data Lineage
- Data Quality
- Business Glossary
- Metadata Management
- AI
url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/apis.yml
use_cases:
- description: Enable data teams to search and find trusted data assets across all data sources using metadata-enriched catalog browsing and search.
  name: Enterprise Data Discovery
- description: Enforce data governance policies, maintain business glossaries, and track stewardship for regulatory compliance and data accountability.
  name: Data Governance Compliance
- description: Power AI applications with structured catalog context from the aggregated context API, enabling accurate data-aware LLM responses.
  name: AI Data Context
- description: Track data flows between systems for compliance auditing, impact analysis, and root cause investigation of data quality issues.
  name: Data Lineage Auditing
- description: Define and score data quality rules across catalog objects for continuous quality monitoring and improvement workflows.
  name: Data Quality Management
---
