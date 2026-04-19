---
api_count: 1
apis:
- description: The Amazon HealthLake API provides programmatic access to create and manage FHIR datastores, import and export health data, and run analytics on FHIR-formatted health records.
  name: Amazon HealthLake API
  slug: amazon-healthlake-api
capabilities:
- description: ''
  name: Amazon Healthlake Health Data Operations
  slug: amazon-healthlake-health-data-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/healthlake/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/healthlake/
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
  url: https://aws.amazon.com/blogs/industries/healthcare/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/healthlake/
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
  type: SDK
  url: https://aws.amazon.com/developer/tools/
- title: ''
  type: CLI
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/index.html
- title: ''
  type: SpectralRules
  url: rules/amazon-healthlake-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-healthlake-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-healthlake-health-data-operations.yaml
created: '2026-03-16'
description: Amazon HealthLake is a HIPAA-eligible service that gives healthcare providers, health insurance companies, and pharmaceutical companies the ability to store, transform, query, and analyze health data at scale in the cloud. It uses the Fast Healthcare Interoperability Resources (FHIR) standard.
features:
- description: Fully compliant with the FHIR R4 standard for healthcare data interoperability.
  name: FHIR Compliance
- description: HIPAA-eligible service for storing and processing protected health information.
  name: HIPAA-Eligible
- description: Bulk import FHIR-formatted health data from Amazon S3 with automated validation.
  name: Integrated Data Import
- description: Export FHIR health data to Amazon S3 for analytics, archiving, or migration.
  name: Data Export
- description: Query FHIR resources using standard FHIR search operations for clinical workflows.
  name: Integrated Search
- description: Built-in de-identification capabilities for removing PHI from health data.
  name: Automated De-identification
- description: Integrated analytics with Amazon Comprehend Medical and other AWS analytics services.
  name: Analytics Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Import and export FHIR health data using S3 as the data source and destination.
  name: Amazon S3
- description: Control access to HealthLake resources using IAM roles and policies.
  name: AWS IAM
- description: Monitor HealthLake operations and performance metrics through CloudWatch.
  name: Amazon CloudWatch
- description: Extract medical entities from unstructured health data using Comprehend Medical.
  name: Amazon Comprehend Medical
- description: Apply SageMaker ML models to FHIR data for predictive health analytics.
  name: Amazon SageMaker
- description: Transform and catalog FHIR health data for analytics using AWS Glue.
  name: AWS Glue
jsonld:
- class_count: 76
  name: Amazon Healthlake Context
  property_count: 0
  slug: amazon-healthlake-context
layout: provider
modified: '2026-04-19'
name: Amazon HealthLake
rules:
- name: Amazon HealthLake API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 2
  slug: amazon-healthlake-spectral-rules
skills: []
slug: amazon-healthlake
solutions: []
tags:
- AWS
- FHIR
- Health Data
- Healthcare
- HIPAA
- Cloud Computing
url: https://raw.githubusercontent.com/api-evangelist/amazon-healthlake/refs/heads/main/apis.yml
use_cases:
- description: Create a centralized FHIR-compliant repository for clinical data from multiple sources.
  name: Clinical Data Repository
- description: Enable interoperable health data exchange between healthcare providers and payers.
  name: Health Data Exchange
- description: Analyze aggregated health data to identify trends and manage population health programs.
  name: Population Health Management
- description: Apply machine learning to FHIR data to generate clinical insights and predictions.
  name: AI-Powered Clinical Insights
- description: Create de-identified research datasets from FHIR health records for clinical studies.
  name: Research Data Platform
---
