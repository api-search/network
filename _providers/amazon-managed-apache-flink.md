---
api_count: 1
apis:
- description: The Amazon Managed Service for Apache Flink API provides programmatic access to create and manage streaming applications, application versions, snapshots, and VPC configurations for Apache Flink workl
  name: Amazon Managed Service for Apache Flink API
  slug: aws-managed-flink-api
capabilities:
- description: Workflow capability for data engineers and analysts to build, manage, and monitor Apache Flink streaming analytics applications on AWS.
  name: Amazon Managed Service for Apache Flink - Streaming Analytics Workflow
  slug: streaming-analytics-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/managed-service-apache-flink/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/managed-flink/
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
  url: https://aws.amazon.com/blogs/big-data/tag/amazon-managed-service-for-apache-flink/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/flink/
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
  url: rules/amazon-managed-apache-flink-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-managed-apache-flink-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/streaming-analytics-workflow.yaml
created: '2026-03-16'
description: Amazon Managed Service for Apache Flink is the easiest way to transform and analyze streaming data in real time with Apache Flink. It enables you to build sophisticated streaming analytics applications using Apache Flink with fully managed infrastructure and pay-as-you-go pricing.
features:
- description: Run Apache Flink applications without managing infrastructure, patching, or capacity planning.
  name: Fully Managed Apache Flink
- description: Automatically scales application parallelism based on streaming data volume.
  name: Auto Scaling
- description: Create point-in-time snapshots of application state for fault tolerance and version management.
  name: Application Snapshots
- description: Deploy Flink applications within a VPC for secure access to private data sources.
  name: VPC Integration
- description: Connect to Kinesis Data Streams, Kinesis Data Firehose, MSK, and S3 as data sources.
  name: Multiple Input Sources
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Use Kinesis streams as input sources for Flink applications.
  name: Amazon Kinesis Data Streams
- description: Connect to managed Kafka clusters as input sources.
  name: Amazon MSK
- description: Read reference data from S3 and write output to S3 buckets.
  name: Amazon S3
- description: Monitor application metrics and logs in CloudWatch.
  name: Amazon CloudWatch
jsonld:
- class_count: 182
  name: Amazon Managed Apache Flink Context
  property_count: 153
  slug: amazon-managed-apache-flink-context
layout: provider
modified: '2026-04-19'
name: Amazon Managed Service for Apache Flink
rules:
- name: Amazon Managed Service for Apache Flink API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 7
  slug: amazon-managed-apache-flink-spectral-rules
skills: []
slug: amazon-managed-apache-flink
solutions: []
tags:
- Apache Flink
- AWS
- Big Data
- Real-Time Processing
- Streaming Analytics
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-apache-flink/refs/heads/main/apis.yml
use_cases:
- description: Build streaming analytics pipelines to analyze data as it arrives from IoT devices, logs, or transactions.
  name: Real-Time Analytics
- description: Process and transform event streams for real-time dashboards and operational monitoring.
  name: Event-Driven Processing
- description: Detect anomalies in streaming data for fraud detection and security monitoring.
  name: Anomaly Detection
- description: Build real-time ETL pipelines to transform and enrich streaming data before loading to destinations.
  name: ETL Pipelines
---
