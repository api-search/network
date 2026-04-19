---
api_count: 1
apis:
- description: The AWS Data Exchange API enables programmatic access to find, subscribe to, and use third-party data products. It supports managing data sets, revisions, assets, jobs, and event actions for cloud-bas
  name: AWS Data Exchange API
  slug: aws-data-exchange-api
capabilities:
- description: ''
  name: Data Marketplace Operations
  slug: data-marketplace-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/data-exchange/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/data-exchange/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/data-exchange/
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
  url: https://aws.amazon.com/blogs/big-data/category/analytics/aws-data-exchange/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/dataexchange/
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
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-data-exchange-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-data-exchange-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-marketplace-operations.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/data-exchange.yaml
created: '2026-03-16'
description: AWS Data Exchange makes it easy to find, subscribe to, and use third-party data in the cloud. Qualified data providers can publish data products consisting of data sets with versioned revisions and assets including S3 snapshots, Redshift data shares, API Gateway APIs, and Lake Formation permissions. Subscribers can find and subscribe to data products directly in the AWS Management Console and use the Data Exchange API to load data into Amazon S3 for analysis with AWS analytics and machine learning services.
features:
- description: Create, update, and manage data sets containing versioned collections of data available for subscription and distribution in the marketplace.
  name: Data Set Management
- description: Organize data into versioned revisions with comments, then finalize and publish them to make data available to subscribers automatically.
  name: Revision Publishing
- description: Support for S3 snapshots, Redshift data shares, API Gateway APIs, Lake Formation permissions, and S3 data access as asset types.
  name: Multi-Format Asset Support
- description: Asynchronous import/export jobs for transferring data between external sources (S3, Redshift) and Data Exchange revisions at scale.
  name: Import and Export Jobs
- description: Configurable event actions that automatically export revision data to S3 when a new revision is published, eliminating manual downloads.
  name: Event-Driven Delivery
- description: Seamlessly list and sell data products in AWS Marketplace with built-in billing, subscription management, and entitlement enforcement.
  name: AWS Marketplace Integration
- description: Control access to data products using AWS IAM policies and resource- level permissions with ARN-based resource identification.
  name: Fine-Grained Access Control
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Primary storage integration for Data Exchange assets — used as both source for imports and destination for exports via job operations.
  name: Amazon S3
- description: Share Redshift tables and views directly through Data Exchange without copying data, enabling live query access for subscribers.
  name: Amazon Redshift
- description: Distribute Lake Formation data permissions through Data Exchange, giving subscribers governed access to data lake resources.
  name: AWS Lake Formation
- description: Expose API-based data products through Data Exchange, allowing subscribers to call APIs for real-time data access.
  name: Amazon API Gateway
- description: Catalog and transform Data Exchange S3 datasets using AWS Glue for ETL and data lake integration workflows.
  name: AWS Glue
- description: Query Data Exchange S3 snapshot data directly with SQL using Athena for serverless analytics on subscribed datasets.
  name: Amazon Athena
- description: Use third-party datasets from Data Exchange as training data for machine learning models in Amazon SageMaker.
  name: Amazon SageMaker
jsonld:
- class_count: 0
  name: Amazon Data Exchange Context
  property_count: 49
  slug: amazon-data-exchange-context
layout: provider
modified: '2026-04-19'
name: Amazon Data Exchange
rules:
- name: Amazon Data Exchange API Rules
  rule_count: 30
  severity_counts:
    error: 13
    hint: 0
    info: 7
    warn: 10
  slug: amazon-data-exchange-spectral-rules
skills: []
slug: amazon-data-exchange
solutions: []
tags:
- AWS
- Data Exchange
- Data Marketplace
- Third-Party Data
- Analytics
- Subscriptions
url: https://raw.githubusercontent.com/api-evangelist/amazon-data-exchange/refs/heads/main/apis.yml
use_cases:
- description: Subscribe to curated third-party datasets from financial data providers, healthcare data aggregators, weather services, and market research firms.
  name: Third-Party Data Acquisition
- description: Publish and sell proprietary datasets to other AWS customers via the marketplace with automated billing and subscription management.
  name: Data Product Monetization
- description: Configure event actions to automatically deliver new data revisions to S3, enabling downstream analytics pipelines to process fresh data.
  name: Automated Data Pipelines
- description: Access high-quality labeled datasets and specialized data products from Data Exchange to train and improve machine learning models.
  name: ML Training Data
- description: Subscribe to compliance reference data including sanctions lists, legal entity identifiers, and regulatory taxonomies via Data Exchange.
  name: Regulatory Compliance Data
---
