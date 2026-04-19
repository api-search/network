---
api_count: 1
apis:
- description: API for creating and managing matching workflows, schema mappings, and ID mapping tables for matching and linking related records across data sources.
  name: Amazon Entity Resolution API
  slug: ''
capabilities:
- description: Unified capability for managing Amazon Entity Resolution resources. Combines Amazon Entity Resolution APIs for Data Analyst workflows in Data Quality.
  name: Amazon Entity Resolution Management
  slug: amazon-entity-resolution-capability
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/entity-resolution/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/entity-resolution/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/entityresolution/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/entity-resolution/faqs/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/entity-resolution
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-entity-resolution-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-entity-resolution-capability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-entity-resolution-vocabulary.yaml
created: '2024-01-15'
description: Amazon Entity Resolution is a service that helps you match and link related records across multiple applications, channels, and data stores using machine learning and configurable matching techniques to identify and consolidate records that refer to the same entity.
features:
- description: Use machine learning models to match records across disparate datasets
  name: ML-Based Matching
- description: Configure deterministic matching rules for exact and fuzzy matching
  name: Rule-Based Matching
- description: Create and manage identity graphs linking records across data sources
  name: ID Mapping
- description: Map input data schemas to standardized formats for consistent matching
  name: Schema Mapping
- description: Enrich records with data from LiveRamp, Unified ID 2.0, and others
  name: Third-Party Data Providers
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Use Glue Data Catalog to discover and access input data sources
  name: AWS Glue
- description: Store matching job input and output data in S3
  name: Amazon S3
- description: Query matching results using Athena SQL
  name: Amazon Athena
- description: Access LiveRamp identity data through the third-party provider integration
  name: LiveRamp
jsonld:
- class_count: 49
  name: Amazon Entity Resolution Context
  property_count: 48
  slug: amazon-entity-resolution-context
layout: provider
modified: '2026-04-19'
name: Amazon Entity Resolution
rules:
- name: Amazon Entity Resolution API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-entity-resolution-spectral-rules
skills: []
slug: amazon-entity-resolution
solutions: []
tags:
- Amazon Web Services
- AWS
- Data Integration
- Data Matching
- Entity Resolution
- Machine Learning
url: https://aws.amazon.com/entity-resolution/
use_cases:
- description: Create a single customer view by matching records across CRM, marketing, and transaction systems
  name: Customer Data Unification
- description: Identify and remove duplicate records from databases and data lakes
  name: Data Deduplication
- description: Link user identities across devices and channels for targeted advertising
  name: Identity Resolution for Advertising
- description: Match patient records across different healthcare providers and systems
  name: Healthcare Record Matching
---
