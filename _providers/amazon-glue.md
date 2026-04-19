---
api_count: 1
apis:
- description: The Amazon Glue API enables programmatic access to create and manage ETL jobs, crawlers, data catalogs, connections, and development endpoints. You can discover data sources, transform data, and orche
  name: Amazon Glue API
  slug: amazon-glue-api
capabilities:
- description: Workflow capability for data engineers building ETL pipelines with Amazon Glue. Covers job management, crawler configuration, data catalog operations, workflow orchestration, and data quality for serv
  name: Amazon Glue Data Integration
  slug: amazon-glue-data-integration
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/glue/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/glue/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/tag/aws-glue/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/glue/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-glue-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-glue-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-glue-data-integration.yaml
created: '2024-01-15'
description: Amazon Glue is a serverless data integration service that makes it simple to discover, prepare, move, and integrate data from multiple sources for analytics, machine learning, and application development. It provides both visual and code-based interfaces for ETL operations and includes a Data Catalog for unified metadata management.
features:
- description: Run ETL jobs without managing infrastructure with automatic scaling and pay-per-use pricing.
  name: Serverless ETL
- description: Build ETL pipelines visually using a drag-and-drop interface without writing code.
  name: Visual ETL Editor
- description: Unified metadata repository for all data assets across S3, databases, and data warehouses.
  name: Data Catalog
- description: Crawlers automatically discover data schemas and populate the Data Catalog.
  name: Automated Schema Discovery
- description: Orchestrate multi-job ETL pipelines with triggers, conditional flows, and scheduling.
  name: Workflow Orchestration
- description: Use machine learning to automate complex data transformation tasks like entity deduplication.
  name: ML Transforms
- description: Centrally manage and enforce data schema evolution with versioning and compatibility checks.
  name: Schema Registry
- description: Define and evaluate data quality rules to validate data during ETL processing.
  name: Data Quality
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Primary data lake storage for Glue ETL input and output.
  name: Amazon S3
- description: Load transformed data into Redshift data warehouse.
  name: Amazon Redshift
- description: Query Data Catalog tables directly with Athena serverless SQL.
  name: Amazon Athena
- description: Process streaming data from Kinesis Data Streams with Glue streaming.
  name: Amazon Kinesis
- description: Ingest and process Kafka streaming data in Glue jobs.
  name: Apache Kafka
- description: Fine-grained access control to Glue Data Catalog resources.
  name: AWS Lake Formation
- description: Connect to relational databases as ETL data sources.
  name: Amazon RDS
jsonld:
- class_count: 418
  name: Amazon Glue Context
  property_count: 330
  slug: amazon-glue-context
layout: provider
modified: '2026-04-19'
name: Amazon Glue
rules:
- name: Amazon Glue API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 2
  slug: amazon-glue-spectral-rules
skills: []
slug: amazon-glue
solutions: []
tags:
- Analytics
- AWS
- Data Catalog
- Data Integration
- Data Pipeline
- ETL
- Serverless
url: https://raw.githubusercontent.com/api-evangelist/amazon-glue/refs/heads/main/apis.yml
use_cases:
- description: Build ETL pipelines to ingest, transform, and load data into Amazon S3 data lakes.
  name: Data Lake ETL
- description: Extract and transform data from multiple sources and load into Amazon Redshift.
  name: Data Warehouse Loading
- description: Maintain a unified data catalog for data discovery across all data assets.
  name: Data Catalog Management
- description: Process streaming data from Kinesis and Kafka with Glue Streaming jobs.
  name: Real-Time Streaming ETL
- description: Prepare and transform training datasets for machine learning using Glue Studio.
  name: Machine Learning Data Prep
---
