---
api_count: 1
apis:
- description: The Amazon Keyspaces API provides programmatic access to manage Cassandra-compatible keyspaces and tables, configure capacity modes, encryption, and point-in-time recovery for serverless Cassandra wor
  name: Amazon Keyspaces API
  slug: ''
capabilities:
- description: Unified workflow capability for Amazon Keyspaces combining resource management and operations.
  name: Amazon Keyspaces Workflow
  slug: amazon-keyspaces-workflow
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/category/database/amazon-keyspaces/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/keyspaces/home
- title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/keyspaces/
- title: ''
  type: SDK
  url: https://aws.amazon.com/tools/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: Portal
  url: https://aws.amazon.com/keyspaces/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/keyspaces/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/keyspaces/pricing/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/keyspaces/getting-started/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/keyspaces/faqs/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-keyspaces-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-keyspaces-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-keyspaces-vocabulary.yaml
created: '2024-01-15'
description: Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra-compatible database service that lets you run Cassandra workloads on AWS without managing servers or software.
features:
- description: Fully compatible with Apache Cassandra drivers, tools, and applications with no code changes required.
  name: Cassandra Compatibility
- description: Automatically scales table throughput and storage up and down based on application traffic.
  name: Serverless Scaling
- description: Continuous backup with PITR enables restoration of tables to any second within the last 35 days.
  name: Point-in-Time Recovery
- description: Data is encrypted at rest by default using AWS managed keys or customer-managed keys via AWS KMS.
  name: Encryption at Rest
- description: Access Amazon Keyspaces from within VPCs using VPC endpoints for enhanced network security.
  name: Virtual Private Cloud (VPC) Support
- description: Choose on-demand or provisioned capacity mode with auto scaling for predictable workloads.
  name: Capacity Modes
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Use customer-managed keys for encryption with AWS Key Management Service.
  name: AWS KMS
- description: Audit all API calls to Amazon Keyspaces for security and compliance.
  name: AWS CloudTrail
- description: Access Keyspaces securely from within your VPC using VPC endpoints.
  name: Amazon VPC
- description: Control access to Keyspaces resources using IAM policies and roles.
  name: AWS Identity and Access Management
jsonld:
- class_count: 2
  name: Amazon Keyspaces Context
  property_count: 7
  slug: amazon-keyspaces-context
layout: provider
modified: '2026-04-19'
name: Amazon Keyspaces
rules:
- name: Amazon Keyspaces API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-keyspaces-spectral-rules
skills: []
slug: amazon-keyspaces
solutions: []
tags:
- AWS
- Cassandra
- Database
- Managed Database
- NoSQL
- Wide Column
url: https://aws.amazon.com/keyspaces/
use_cases:
- description: Store high-volume sensor data and telemetry from IoT devices with wide-column schema.
  name: IoT Data Storage
- description: Track user events, clickstreams, and behavioral data at massive scale.
  name: User Activity Tracking
- description: Manage time-series data for monitoring, metrics, and log aggregation.
  name: Time-Series Data
- description: Lift and shift existing Cassandra applications to a fully managed cloud service.
  name: Migrate Cassandra Workloads
---
