---
api_count: 1
apis:
- description: The Amazon Macie API provides programmatic access to create and manage the resources, data, and activities for discovering, classifying, and protecting sensitive data stored in Amazon S3 buckets. Cove
  name: Amazon Macie API
  slug: amazon-macie-api
capabilities:
- description: Workflow capability for security and compliance teams to discover sensitive data, investigate findings, and manage data security posture in Amazon S3 using Amazon Macie.
  name: Amazon Macie - Data Security Operations
  slug: data-security-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/macie/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/macie/
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
  url: https://aws.amazon.com/blogs/security/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/macie/
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
  url: rules/amazon-macie-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-macie-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-security-operations.yaml
created: '2024-01-15'
description: Amazon Macie is a data security service that discovers sensitive data by using machine learning and pattern matching, provides visibility into data security risks, and enables automated protection against those risks. Macie automates the discovery of sensitive data, such as personally identifiable information (PII) and financial data, to provide you with a better understanding of the data that your organization stores in Amazon S3.
features:
- description: Automatically discovers and classifies sensitive data in S3 using ML and pattern matching.
  name: Automated Sensitive Data Discovery
- description: Detects personally identifiable information (PII), financial data, and credentials in S3 objects.
  name: PII and Financial Data Detection
- description: Create custom regex patterns to detect organization-specific sensitive data types.
  name: Custom Data Identifiers
- description: Generates detailed findings with severity ratings for all detected sensitive data exposures.
  name: Data Security Findings
- description: Provides visibility into bucket configurations, encryption status, and public access settings.
  name: S3 Bucket Security Posture
- description: Manage Macie across multiple AWS accounts from a central administrator account.
  name: Multi-Account Support
- description: Define allow lists to suppress false positives for known acceptable sensitive data patterns.
  name: Allow Lists
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Scans S3 buckets to discover and classify sensitive data objects.
  name: Amazon S3
- description: Sends findings to Security Hub for centralized security posture management.
  name: AWS Security Hub
- description: Publishes findings events to EventBridge for automated remediation workflows.
  name: Amazon EventBridge
- description: Integrates with Organizations for multi-account sensitive data discovery.
  name: AWS Organizations
- description: Publishes metrics and logs to CloudWatch for monitoring and alerting.
  name: Amazon CloudWatch
jsonld:
- class_count: 301
  name: Amazon Macie Context
  property_count: 331
  slug: amazon-macie-context
layout: provider
modified: '2026-04-19'
name: Amazon Macie
rules:
- name: Amazon Macie API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 7
  slug: amazon-macie-spectral-rules
skills: []
slug: amazon-macie
solutions: []
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
url: https://raw.githubusercontent.com/api-evangelist/amazon-macie/refs/heads/main/apis.yml
use_cases:
- description: Discover and inventory personal data across S3 to support GDPR data mapping and compliance reporting.
  name: GDPR and Privacy Compliance
- description: Detect credit card numbers and financial data stored in S3 to maintain PCI-DSS compliance.
  name: PCI-DSS Compliance
- description: Identify sensitive data stored in public or insufficiently protected S3 buckets.
  name: Data Loss Prevention
- description: Quickly determine if sensitive data was exposed in an S3 bucket involved in a security incident.
  name: Security Incident Response
- description: Build a data inventory and understand where sensitive data lives across the organization.
  name: Data Governance
---
