---
api_count: 1
apis:
- description: The AWS Lake Formation API provides programmatic access to build and manage data lakes with centralized governance. It enables developers to register data sources, configure data permissions, manage d
  name: AWS Lake Formation API
  slug: ''
capabilities:
- description: Unified workflow capability for AWS Lake Formation combining resource management and operations.
  name: AWS Lake Formation Workflow
  slug: amazon-lakeformation-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Portal
  url: https://aws.amazon.com/lake-formation/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lake-formation/
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
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/lakeformation/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-lakeformation-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-lakeformation-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-lakeformation-vocabulary.yaml
created: '2024-01-15'
description: AWS Lake Formation is a fully managed service that makes it easy to build, secure, and manage data lakes. It simplifies and automates many of the complex manual steps usually required to create data lakes, including collecting, cleansing, cataloging, and securely sharing data, with centralized governance and fine-grained access control across your analytics and machine learning services.
features:
- description: Set up a secure data lake in days with centralized governance and automated data ingestion.
  name: Data Lake Setup
- description: ACID transactions, row-level security, and automatic compaction for governed tables.
  name: Governed Tables
- description: Column, row, and cell-level security policies enforced across analytics engines.
  name: Fine-Grained Access Control
- description: Pre-built workflows to ingest data from common data sources into the data lake.
  name: Blueprints
- description: Share data across accounts and organizations with fine-grained permissions.
  name: Data Sharing
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Store and manage data lake content in S3 with Lake Formation governance.
  name: Amazon S3
- description: Catalog data and run ETL jobs with Glue, governed by Lake Formation.
  name: AWS Glue
- description: Process large datasets with EMR Spark, respecting Lake Formation permissions.
  name: Amazon EMR
- description: Visualize data lake content with QuickSight enforcing Lake Formation policies.
  name: Amazon QuickSight
jsonld:
- class_count: 2
  name: Amazon Lakeformation Context
  property_count: 7
  slug: amazon-lakeformation-context
layout: provider
modified: '2026-04-19'
name: AWS Lake Formation
rules:
- name: AWS Lake Formation API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-lakeformation-spectral-rules
skills: []
slug: amazon-lakeformation
solutions: []
tags:
- Analytics
- AWS
- Data Lake
- Governance
url: https://aws.amazon.com/lake-formation/
use_cases:
- description: Build a centralized data lake with governed access for analytics teams.
  name: Enterprise Data Lake
- description: Implement a data mesh architecture with cross-account data sharing and governance.
  name: Data Mesh
- description: Enforce data access policies for GDPR, HIPAA, and other compliance requirements.
  name: Compliance Governance
---
