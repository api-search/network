---
api_count: 1
apis:
- description: The ADOC API provides programmatic access to data observability features including alerts, data quality rules, pipeline monitoring, data lineage, users, groups, roles, and permissions within the Accel
  name: Acceldata Data Observability Cloud API
  slug: adoc-api
capabilities:
- description: ''
  name: Data Observability
  slug: data-observability
common:
- title: ''
  type: Website
  url: https://www.acceldata.io/
- title: ''
  type: Portal
  url: https://accounts.acceldata.app/login
- title: ''
  type: Documentation
  url: https://docs.acceldata.io/
- title: ''
  type: GettingStarted
  url: https://docs.acceldata.io/api/introduction
- title: ''
  type: Pricing
  url: https://www.acceldata.io/pricing
- title: ''
  type: Blog
  url: https://www.acceldata.io/blog
- title: ''
  type: PrivacyPolicy
  url: https://www.acceldata.io/privacy-policy
- title: ''
  type: TermsOfService
  url: https://www.acceldata.io/terms-of-use
- title: ''
  type: SpectralRules
  url: rules/acceldata-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-observability.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/acceldata-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/acceldata-adoc-api-context.jsonld
created: '2025-02-24'
description: Acceldata is an agentic data management platform that helps enterprises monitor, govern, and optimize data across cloud, lakehouse, and hybrid environments. The platform combines AI-powered agents with data observability to proactively detect issues, trace root causes, and automate remediation workflows. Key products include ADM (Agentic Data Management), ADOC (Acceldata Data Observability Cloud), Pulse for Hadoop environments, and Agent Studio for building custom AI agents. It supports integrations with Snowflake, Databricks, AWS, GCP, Azure, and Hadoop.
features:
- description: AI-powered agents that proactively detect issues, trace root causes, and automate data quality remediation workflows
  name: Agentic Data Management
- description: Multi-variate anomaly detection, column-level profiling, and proactive monitoring across all data platforms
  name: Data Quality Monitoring
- description: End-to-end data lineage visualization with schema change management and column-level impact analysis
  name: Data Lineage
- description: Real-time SLA monitoring, bottleneck identification, and root cause analysis for data pipelines
  name: Pipeline Health Monitoring
- description: Visibility into data spending, budget optimization, chargebacks, and cost forecasting across cloud environments
  name: Data Cost Management
- description: Natural language interface with contextual memory for querying data quality and observability insights
  name: Business Notebook
- description: Low-code environment for building and deploying custom AI agents for data management workflows
  name: Agent Studio
- description: Bring Your Own Large Language Model for enterprise-controlled AI inference within data operations
  name: BYOLLM Support
- description: Exabyte-scale, AI-aware processing engine supporting cloud hyperscalers and on-premises deployments
  name: xLake Reasoning Engine
image: /assets/icons/acceldata.png
integrations:
- description: Native integration for monitoring Snowflake data quality, query performance, and cost optimization
  name: Snowflake
- description: Integration for observing Databricks lakehouse pipelines, job health, and data quality
  name: Databricks
- description: Support for AWS data services including S3, Redshift, Glue, EMR, and Athena
  name: AWS
- description: Integration with GCP data services including BigQuery, Dataflow, and Cloud Storage
  name: Google Cloud Platform
- description: Integration with Azure Synapse, Azure Data Factory, and Azure Data Lake Storage
  name: Microsoft Azure
- description: Dedicated Pulse product for Hadoop ecosystem monitoring including HDFS, YARN, Hive, and Spark
  name: Hadoop / Apache
jsonld:
- class_count: 55
  name: Acceldata Adoc Api Context
  property_count: 5
  slug: acceldata-adoc-api-context
layout: provider
modified: '2026-04-19'
name: Acceldata
rules:
- name: Acceldata API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 12
  slug: acceldata-spectral-rules
skills: []
slug: acceldata
solutions: []
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
url: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/apis.yml
use_cases:
- description: Continuously monitor and automatically remediate data quality issues across cloud and hybrid environments
  name: Data Quality Assurance
- description: Validate data completeness, consistency, and accuracy during cloud migration projects
  name: Cloud Migration Validation
- description: Ensure data pipelines produce clean, reliable, and AI-ready datasets for training and inference
  name: AI and LLM Data Readiness
- description: Identify and reduce wasteful data pipeline and infrastructure costs with granular usage analytics
  name: Cost Optimization and FinOps
- description: Automatically detect and resolve discrepancies between source and target systems across platforms
  name: Data Reconciliation
- description: Track data lineage and access patterns to support regulatory compliance and data governance programs
  name: Compliance and Data Governance
---
