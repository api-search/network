---
api_count: 1
apis:
- description: The AWS HealthImaging API provides programmatic access to create and manage datastores, image sets, and DICOM import jobs for storing and retrieving medical imaging data at scale. The API is HIPAA-eli
  name: AWS HealthImaging API
  slug: aws-healthimaging-api
capabilities:
- description: ''
  name: Amazon Healthimaging Medical Imaging Operations
  slug: amazon-healthimaging-medical-imaging-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/healthimaging/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/healthimaging/
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
  url: https://console.aws.amazon.com/healthimaging/
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
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/index.html
- title: ''
  type: SpectralRules
  url: rules/amazon-healthimaging-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-healthimaging-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-healthimaging-medical-imaging-operations.yaml
created: '2026-03-16'
description: AWS HealthImaging is a HIPAA-eligible service that helps healthcare providers and their software partners store, transform, and apply machine learning to medical images. It provides sub-second image retrieval and enables scaling from hundreds to millions of medical images.
features:
- description: Fully HIPAA-eligible service for storing protected health information including medical images.
  name: HIPAA-Eligible Storage
- description: Native support for DICOM format, the standard for medical imaging data exchange and storage.
  name: DICOM Support
- description: Optimized storage architecture enabling sub-second retrieval of medical images at any scale.
  name: Sub-Second Retrieval
- description: Built-in support for applying machine learning models to medical imaging data for analysis.
  name: Machine Learning Integration
- description: Create and manage datastores that scale from hundreds to millions of medical images.
  name: Scalable Datastores
- description: Organize medical images into sets with comprehensive metadata management and versioning.
  name: Image Set Management
- description: DICOM import jobs enable bulk import of medical imaging data from Amazon S3.
  name: Bulk Import
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Import medical imaging data from S3 buckets using DICOM import jobs.
  name: Amazon S3
- description: Control access to HealthImaging resources using IAM roles and policies.
  name: AWS IAM
- description: Monitor HealthImaging operations and performance metrics through CloudWatch.
  name: Amazon CloudWatch
- description: Integrate with HealthLake for combining medical imaging with FHIR health records.
  name: AWS HealthLake
- description: Apply SageMaker ML models to medical images for AI-powered analysis and diagnostics.
  name: Amazon SageMaker
jsonld:
- class_count: 113
  name: Amazon Healthimaging Context
  property_count: 0
  slug: amazon-healthimaging-context
layout: provider
modified: '2026-04-19'
name: Amazon HealthImaging
rules:
- name: Amazon HealthImaging API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 2
  slug: amazon-healthimaging-spectral-rules
skills: []
slug: amazon-healthimaging
solutions: []
tags:
- AWS
- Healthcare
- HIPAA
- Machine Learning
- Medical Imaging
- DICOM
url: https://raw.githubusercontent.com/api-evangelist/amazon-healthimaging/refs/heads/main/apis.yml
use_cases:
- description: Streamline radiology workflows by centralizing medical image storage and enabling rapid retrieval.
  name: Radiology Workflow
- description: Apply machine learning models to medical images for automated diagnostic assistance.
  name: AI-Powered Diagnostics
- description: Archive medical imaging data in a HIPAA-eligible, scalable environment with long-term retention.
  name: Healthcare Data Archiving
- description: Centralize medical imaging data from multiple healthcare sites for unified access and analysis.
  name: Multi-Site Imaging
- description: Support clinical research by providing scalable access to large medical imaging datasets.
  name: Clinical Research
---
